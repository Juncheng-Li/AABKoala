from django.db import models


class Result(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    AuditID = models.CharField(max_length=45)
    RevisionNumber = models.CharField(max_length=45)
    FacilityName = models.CharField(max_length=100)
    FacilityID = models.CharField(max_length=45)
    Auditor1 = models.CharField(max_length=45)
    Auditor2 = models.CharField(max_length=45)
    Auditor3 = models.CharField(max_length=45)
    AuditDate = models.DateTimeField()
    RepDate = models.CharField(max_length=45)
    LinacModel = models.CharField(max_length=45)
    LinacManufacturer = models.CharField(max_length=45)
    PlanningSystemManufacturer = models.CharField(max_length=45)
    tps = models.CharField(max_length=45)
    Algorithm = models.CharField(max_length=45)
    kqFac = models.CharField(max_length=10)
    ACDS = models.CharField(max_length=10)
    Phantom = models.CharField(max_length=45)

    class Meta:
        ordering = ['created']