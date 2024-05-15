# ... from django.core.mail import send_mail #
def post_share(request, post_id): 
    # Retrieve post by id 
    post = get_object_or_404( Post, id=post_id, status=Post.Status.PUBLISHED ) 
    sent = False 
    if request.method == 'POST': # Form was submitted 
        form = EmailPostForm(request.POST) 
    if form.is_valid(): # Form fields passed validation
        cd = form.cleaned_data 
        post_url = request.build_absolute_uri( post.get_absolute_url() ) 
        subject = ( f"{cd['name']} ({cd['email']}) " f"recommends you read {post.title}" ) 
        message = ( f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}" ) 
        send_mail( subject=subject, message=message, from_email=None, recipient_list=[cd['to']] ) 
        sent = True 
    else: 
        form = EmailPostForm() 
    return render( request, 'blog/post/share.html', { 'post': post, 'form': form, 'sent': sent } )