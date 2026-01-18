from django.db import models
import os
import hashlib
import hmac


# Create your models here.
class LegalRep(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    cpf_hash = models.CharField(max_length=255, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15)
    descriptor = models.JSONField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.cpf and self.cpf.find("*") == -1:
            secret_key = os.environ.get("SECRET_KEY", "default_secret_key")
            self.cpf_hash = hmac.new(
                key=secret_key.encode(),
                msg=self.cpf.encode(),
                digestmod=hashlib.sha256,
            ).hexdigest()

        self.cpf = self.cpf[:6] + "*****"  # Masking CPF for privacy

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Responsável Legal"
        verbose_name_plural = "Responsáveis Legais"
