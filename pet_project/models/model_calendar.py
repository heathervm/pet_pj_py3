from .model_people import *
from .model_horse import *

class Lesson(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE, null="False")
    paid = (
        ('Y', 'yes'), 
        ('N', 'no'), 
        ('CR', 'credit'))
    compensation = models.CharField(choices = paid, max_length=2)
    arrival = (
        ('Y', 'yes'),
        ('N', 'no'),
        ('L', 'late'))
    arrived = models.CharField(choices = arrival, max_length=2)
    #discipline = models.CharField(max_length = 300)
    #email = models.EmailField(max_length= 254, null = "True")
    #phone_number = models.IntegerField(default=1234567890)
    training_plans = models.ForeignKey(Plan, on_delete=models.CASCADE, null="True", blank = "True")
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, null="True", blank = "True")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null="True", blank="True")
    def __str__(self):
        return (self.name)

class studentCalendar(models.Model):
    student  = models.ForeignKey(Person, blank="False", on_delete=models.CASCADE, null="False")
    date = models.DateTimeField(blank="False", editable="True")
    lesson = models.ForeignKey(Lesson, blank="True", on_delete=models.CASCADE, null="True")
    


class careCalendar(models.Model):
    date = models.DateTimeField(blank="False", editable="True")
    vet_care = models.ForeignKey(veterinaryCare, on_delete=models.CASCADE, null=True, blank=True)
    farrier_care = models.ForeignKey(farrierCare, on_delete=models.CASCADE, null=True, blank=True)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, null = "True")
    
