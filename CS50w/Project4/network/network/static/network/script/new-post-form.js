document.addEventListener('DOMContentLoaded', function() {

    // get the new post form 
    const newPostForms = document.querySelectorAll('#post-form');

    // add event for forms
    newPostForms.forEach((postForm) => {

        postForm.addEventListener('submit', function(e) {

            // get post content
            const postContent = this.querySelector('#post');

            if (!checkPostContent(postContent.value)) {
                // change the bg color of input(textarea)
                postForm.parentElement.style.backgroundColor = "rgb(242,0,60)";

                // clear the input is from spaces 
                postContent.value = '';

                // change the placeholder of postconetent container to an error
                postContent.placeholder = "nothing here, write something!";
                postContent.classList.add('post-change-placeolder-color');

                // prevent from submiting 
                e.preventDefault()
                return false
            }
        });
    });
});

function checkPostContent(post) {

    if (post === '' || post.trim() === '')
        return false

    // if the post has worlds
    return true

}