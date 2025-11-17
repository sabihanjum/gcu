from rest_framework import serializers
from django.utils import timezone
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    # declare datetime fields explicitly if present on the model
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    published = serializers.SerializerMethodField(read_only=True)

    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'published_date']

    def get_published(self, obj):
        val = getattr(obj, 'published', None)
        if val is None:
            return None
        if timezone.is_aware(val):
            val = timezone.localtime(val)
        return val.date().isoformat()