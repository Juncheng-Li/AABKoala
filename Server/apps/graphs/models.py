from django.db import models


class Result(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    AuditID = models.CharField(max_length=45)
    RevisionNumber = models.CharField(max_length=45, null=True)
    FacilityName = models.CharField(max_length=100)
    FacilityID = models.CharField(max_length=45, null=True)
    Auditor1 = models.CharField(max_length=45)
    Auditor2 = models.CharField(max_length=45, null=True)
    Auditor3 = models.CharField(max_length=45, null=True)
    AuditDate = models.DateField(null=True)
    RepDate = models.CharField(max_length=45, null=True)
    LinacModel = models.CharField(max_length=45, null=True)
    LinacManufacturer = models.CharField(max_length=45, null=True)
    PlanningSystemManufacturer = models.CharField(max_length=45, null=True)
    tps = models.CharField(max_length=45, null=True)
    Algorithm = models.CharField(max_length=45, null=True)
    kqFac = models.CharField(max_length=10, null=True)
    ACDS = models.CharField(max_length=10, null=True)
    Phantom = models.CharField(max_length=45, null=True)
    user = models.ForeignKey('auth.User', related_name='result', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        db_table = 'result'


class FacilityOutput(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    energy_6 = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_10 = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_15 = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_18 = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_6FFF = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_10FFF = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    result = models.ForeignKey(Result, related_name='facilityOutput', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        db_table = 'facilityoutput'


class TPR(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    energy_6 = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_10 = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_15 = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_18 = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_6FFF = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    energy_10FFF = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    result = models.ForeignKey(Result, related_name='TPR', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        db_table = 'tpr'


class Nds_3dcrt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    code_101106 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_110106 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_205106 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_208106 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_205206 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_208206 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_205306 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_208306 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_303106 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_305106 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_403106 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_405106 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_103110 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_110110 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_303110 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_305110 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_403110 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_405110 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_103115 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_110115 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_303115 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_305115 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_403115 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_405115 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_103118 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_110118 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_303118 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_305118 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_403118 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_405118 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_101105 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_110105 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_303105 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_305105 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_103109 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_110109 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_303109 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_305109 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    result = models.ForeignKey(Result, related_name='Nds_3dcrt', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        db_table = 'nds_3dcrt'

class Nds_3dcrt_misdelivery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    code_101106 = models.SmallIntegerField(null=True)
    code_110106 = models.SmallIntegerField(null=True)
    code_205106 = models.SmallIntegerField(null=True)
    code_208106 = models.SmallIntegerField(null=True)
    code_205206 = models.SmallIntegerField(null=True)
    code_208206 = models.SmallIntegerField(null=True)
    code_205306 = models.SmallIntegerField(null=True)
    code_208306 = models.SmallIntegerField(null=True)
    code_303106 = models.SmallIntegerField(null=True)
    code_305106 = models.SmallIntegerField(null=True)
    code_403106 = models.SmallIntegerField(null=True)
    code_405106 = models.SmallIntegerField(null=True)
    code_103110 = models.SmallIntegerField(null=True)
    code_110110 = models.SmallIntegerField(null=True)
    code_303110 = models.SmallIntegerField(null=True)
    code_305110 = models.SmallIntegerField(null=True)
    code_403110 = models.SmallIntegerField(null=True)
    code_405110 = models.SmallIntegerField(null=True)
    code_103115 = models.SmallIntegerField(null=True)
    code_110115 = models.SmallIntegerField(null=True)
    code_303115 = models.SmallIntegerField(null=True)
    code_305115 = models.SmallIntegerField(null=True)
    code_403115 = models.SmallIntegerField(null=True)
    code_405115 = models.SmallIntegerField(null=True)
    code_103118 = models.SmallIntegerField(null=True)
    code_110118 = models.SmallIntegerField(null=True)
    code_303118 = models.SmallIntegerField(null=True)
    code_305118 = models.SmallIntegerField(null=True)
    code_403118 = models.SmallIntegerField(null=True)
    code_405118 = models.SmallIntegerField(null=True)
    code_101105 = models.SmallIntegerField(null=True)
    code_110105 = models.SmallIntegerField(null=True)
    code_303105 = models.SmallIntegerField(null=True)
    code_305105 = models.SmallIntegerField(null=True)
    code_103109 = models.SmallIntegerField(null=True)
    code_110109 = models.SmallIntegerField(null=True)
    code_303109 = models.SmallIntegerField(null=True)
    code_305109 = models.SmallIntegerField(null=True)
    result = models.ForeignKey(Result, related_name='Nds_3dcrt_misdelivery', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        db_table = 'nds_3dcrt_misdelivery'


class Graph(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=250)
    fileName = models.CharField(max_length=250)
    result = models.ManyToManyField('Result')

    class Meta:
        ordering = ['created']
        db_table = 'graph'


class Nds_imrt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    code_c6_p11_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p12_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p13_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p14_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p15_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p16_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p17_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p11_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p12_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p13_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p14_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p15_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p16_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p17_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p11_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p12_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p13_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p14_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p15_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p17_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p18_6 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p11_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p12_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p13_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p14_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p15_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p16_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c6_p17_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p11_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p12_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p13_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p14_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p15_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p16_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c7_p17_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p11_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p12_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p13_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p14_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p15_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p17_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    code_c8_p18_10 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    result = models.ForeignKey(Result, related_name='Nds_imrt', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        db_table = 'nds_imrt'


class Nds_imrt_misdelivery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    code_c6_p11_6 = models.SmallIntegerField(null=True)
    code_c6_p12_6 = models.SmallIntegerField(null=True)
    code_c6_p13_6 = models.SmallIntegerField(null=True)
    code_c6_p14_6 = models.SmallIntegerField(null=True)
    code_c6_p15_6 = models.SmallIntegerField(null=True)
    code_c6_p16_6 = models.SmallIntegerField(null=True)
    code_c6_p17_6 = models.SmallIntegerField(null=True)
    code_c7_p11_6 = models.SmallIntegerField(null=True)
    code_c7_p12_6 = models.SmallIntegerField(null=True)
    code_c7_p13_6 = models.SmallIntegerField(null=True)
    code_c7_p14_6 = models.SmallIntegerField(null=True)
    code_c7_p15_6 = models.SmallIntegerField(null=True)
    code_c7_p16_6 = models.SmallIntegerField(null=True)
    code_c7_p17_6 = models.SmallIntegerField(null=True)
    code_c8_p11_6 = models.SmallIntegerField(null=True)
    code_c8_p12_6 = models.SmallIntegerField(null=True)
    code_c8_p13_6 = models.SmallIntegerField(null=True)
    code_c8_p14_6 = models.SmallIntegerField(null=True)
    code_c8_p15_6 = models.SmallIntegerField(null=True)
    code_c8_p17_6 = models.SmallIntegerField(null=True)
    code_c8_p18_6 = models.SmallIntegerField(null=True)
    code_c6_p11_10 = models.SmallIntegerField(null=True)
    code_c6_p12_10 = models.SmallIntegerField(null=True)
    code_c6_p13_10 = models.SmallIntegerField(null=True)
    code_c6_p14_10 = models.SmallIntegerField(null=True)
    code_c6_p15_10 = models.SmallIntegerField(null=True)
    code_c6_p16_10 = models.SmallIntegerField(null=True)
    code_c6_p17_10 = models.SmallIntegerField(null=True)
    code_c7_p11_10 = models.SmallIntegerField(null=True)
    code_c7_p12_10 = models.SmallIntegerField(null=True)
    code_c7_p13_10 = models.SmallIntegerField(null=True)
    code_c7_p14_10 = models.SmallIntegerField(null=True)
    code_c7_p15_10 = models.SmallIntegerField(null=True)
    code_c7_p16_10 = models.SmallIntegerField(null=True)
    code_c7_p17_10 = models.SmallIntegerField(null=True)
    code_c8_p11_10 = models.SmallIntegerField(null=True)
    code_c8_p12_10 = models.SmallIntegerField(null=True)
    code_c8_p13_10 = models.SmallIntegerField(null=True)
    code_c8_p14_10 = models.SmallIntegerField(null=True)
    code_c8_p15_10 = models.SmallIntegerField(null=True)
    code_c8_p17_10 = models.SmallIntegerField(null=True)
    code_c8_p18_10 = models.SmallIntegerField(null=True)
    result = models.ForeignKey(Result, related_name='Nds_imrt_misdelivery', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        db_table = 'nds_imrt_misdelivery'
