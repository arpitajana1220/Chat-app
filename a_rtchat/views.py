from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import Http404

@login_required
def chat_view(request, chatroom_name='public-chat'):
    chat_groups = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_groups.chat_messages.all()[:30]    
    form = ChatmessageCreateForm()

    other_user = None
    if chat_groups.is_private:
        if request.user not in chat_groups.members.all():
            return Http404()
        for member in chat_groups.members.all():
            if member != request.user:
                other_user = member
                break

    
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_groups
            message.save()
            context = {
                'message': message,
                'user': request.user
                }
            return render(request, 'a_rtchat/partials/chat_message_p.html',context)
            # return redirect('home')
    context = {
        'chat_messages': chat_messages, 
        'form': form,
        'other_user': other_user,
        'chatroom_name': chatroom_name,
        }
    
    return render(request, 'a_rtchat/chat.html',context)

def get_or_create_chatroom(request, username):
    if request.user.username == username:
        return redirect('home')
    
    other_user = User.objects.get(username = username)
    my_private_chatrooms = request.user.chat_groups.filter(is_private=True)
    
    if my_private_chatrooms.exists():
        for chatroom in my_private_chatrooms:
            if other_user in chatroom.members.all():
                return redirect('chatroom', chatroom.group_name)
   
    chatroom = ChatGroup.objects.create( is_private = True )
    chatroom.members.add(other_user, request.user)   
    return redirect('chatroom', chatroom.group_name)