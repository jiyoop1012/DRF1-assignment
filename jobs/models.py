from django.db import models

class JobOffer(models.Model):
    company_name    = models.CharField(max_length=60)
    company_email   = models.CharField(max_length=200)
    job_title       = models.CharField(max_length=60)
    job_description = models.TextField(blank=True)
    salary          = models.PositiveIntegerField()
    city            = models.CharField(max_length=60)
    state           = models.CharField(max_length=60)
    created_at      = models.DateTimeField(auto_now_add=True)
    available       = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company_name} {self.job_title}"
