from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    map_image = models.ImageField(upload_to='maps/', blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.IntegerField()
    room_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.building.name} Floor {self.floor}"
    
class Node(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    floor = models.IntegerField()
    node_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Node {self.id} - {self.building.name} Floor {self.floor}"
    
class Edge(models.Model):
    start_node = models.ForeignKey(Node, related_name='start_edges', on_delete=models.CASCADE)
    end_node = models.ForeignKey(Node, related_name='end_edges', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"Edge from {self.start_node.id} to {self.end_node.id}"  