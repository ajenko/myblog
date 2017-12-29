from django.shortcuts import render
from django.views.generic import View

from .models import ChatMessage
# Create your views here.


class ChatView(View):

	def get(self, request):
		# show last 10 messages, ordered most-recent-last
		chat_queryset = ChatMessage.objects.order_by('-created')[:10]
		chat_messages_count = len(chat_queryset)
		if chat_messages_count > 0:
			first_message_id = chat_queryset[len(chat_queryset)-1].id
		else:
			first_message_id = -1
		previous_id = -1
		if first_message_id != -1:
			try:
				previous_id = ChatMessage.objects.filter(
					pk__lt=first_message_id).order_by('-pk')[:1][0].id
			except IndexError:
				previous_id = -1
		chat_messages = reversed(chat_queryset)
		context = {
			'chat_messages': chat_messages,
			'first_message_id': previous_id,
		}

		return render(request, 'chatroom.html', context)