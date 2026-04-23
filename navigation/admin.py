from django.contrib import admin

from django.contrib import admin
from .models import Building, Room, Node, Edge

admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Node)
admin.site.register(Edge)
