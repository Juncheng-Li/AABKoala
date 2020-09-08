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
    user = models.ForeignKey('auth.User', related_name='result', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class FacilityOutput(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    energy_6 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_10 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_15 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_18 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_6FFF = models.DecimalField(max_digits=6, decimal_places=3)
    energy_10FFF = models.DecimalField(max_digits=6, decimal_places=3)
    result = models.ForeignKey(Result, related_name='facilityOutput', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class TPR(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    energy_6 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_10 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_15 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_18 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_6FFF = models.DecimalField(max_digits=6, decimal_places=3)
    energy_10FFF = models.DecimalField(max_digits=6, decimal_places=3)
    result = models.ForeignKey(Result, related_name='TPR', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Reading(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    Reading_101106 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_110106 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_205106 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_208106 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_205206 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_208206 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_205306 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_208306 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_303106 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_305106 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_403106 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_405106 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_103110 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_110110 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_303110 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_305110 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_403110 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_405110 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_103115 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_110115 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_303115 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_305115 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_403115 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_405115 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_103118 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_110118 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_303118 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_305118 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_403118 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_405118 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_101105 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_110105 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_303105 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_305105 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_103109 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_110109 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_303109 = models.DecimalField(max_digits=5, decimal_places=2)
    Reading_305109 = models.DecimalField(max_digits=5, decimal_places=2)
    result = models.ForeignKey(Result, related_name='Reading', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
