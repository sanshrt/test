from django.contrib import admin
from .models import Message

# Custom action to mark selected messages as read
def mark_as_read(modeladmin, request, queryset):
    queryset.update(is_read=True)

mark_as_read.short_description = "Mark selected messages as read"  # Action label

class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'timestamp', 'is_read', 'user')  # Columns to display
    list_filter = ('user', 'timestamp', 'is_read')  # Filters for messages
    actions = [mark_as_read]  # Add custom actions
    search_fields = ['user__username', 'content']  # Search functionality by username or content

    # Make the 'user' field clickable in the admin list view
    list_display_links = ('user',)  # This will make the username clickable

    # Modify the queryset to show messages for the selected user in admin
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # If the admin is viewing messages for a specific user, filter by that user
        if 'user__id' in request.GET:
            user_id = request.GET['user__id']
            queryset = queryset.filter(user_id=user_id)
        
        return queryset

    # To prevent repeating the username for each message
    def user(self, obj):
        return obj.user.username  # Show username, not the whole user object
    user.admin_order_field = 'user'  # Allows sorting by username
    user.short_description = 'Username'  # Display name in the admin panel

# Register the Message model with the custom admin configuration
admin.site.register(Message, MessageAdmin)
