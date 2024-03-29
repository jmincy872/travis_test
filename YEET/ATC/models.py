from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=100)
    isATC = models.BooleanField(default=False)
    isGate = models.BooleanField(default=False)


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # TODO: add salt and hash
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)

    def hasATCPerm(self):
        return self.role.isATC

    def hasGatePerm(self):
        return self.role.isGate


class Airport(models.Model):
    name = models.CharField(max_length=100)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def getRunways(self):
        return Runway.objects.filter(airport=self)

    def getGate(self):
        return Gate.objects.filter(airport=self)

    def getAirlines(self):
        return Airline.objects.filter(airport=self)


class Airline(models.Model):
    name = models.CharField(max_length=100)
    airport = models.ManyToManyField("Airport")

    def getPlanes(self):
        return Plane.objects.filter(airline=self)

      
class Plane(models.Model):
    identifier = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    currentPassengerCount = models.IntegerField()
    maxPassengerCount = models.IntegerField()
    airline = models.ForeignKey("Airline",null=True,on_delete=models.SET_NULL)
    gate = models.OneToOneField("Gate", null=True,on_delete=models.SET_NULL)
    runway = models.OneToOneField("Runway", null=True,on_delete=models.SET_NULL)

    def getAirline(self):
        return self.airline
    def getGate(self):
        return self.gate
    def getRunway(self):
        return self.runway


class Runway(models.Model):
    identifier = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    def getPlane(self):
        return self.plane

    def getAirport(self):
        return self.airport


class Gate(models.Model):
    identifier = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    def getPlane(self):
        return self.plane

    def getAirport(self):
        return self.airport
