

document.addEventListener('DOMContentLoaded', function() {
    
    // get the csrfToken 
    let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0];

    // get the new-post buttons
    const newPostButtons = document.querySelectorAll('#new-post');
    newPostButtons.forEach((PostButton) => {
        PostButton.addEventListener('click', function(event) { 
            // preventing the page from loading
            event.preventDefault();

            // now i need make a liitle page to for the user to make a new post.
            const newPostForm = document.querySelector('#new-post-form');

            // add the class that shows the element 
            newPostForm.classList.add('show-item');

            // remove the class that remove the item 
            newPostForm.classList.remove('remove-item');

            // stop the user from scrollin 
            document.querySelector('body').style.overflow = "hidden";

        });
    });

    // new form alert remove
    const removeAlertButton = document.querySelectorAll('#remove-new-post-form');
    removeAlertButton.forEach((Button) => {

        Button.addEventListener('click', function() {
    
            // set new post form animation state to pause 
    
            const newPostForm = this.parentElement.parentElement;
    
            // add the remove item class 
            newPostForm.classList.add('remove-item');
    
            // remove the show item class 
            newPostForm.classList.remove('show-item');
    
            // continue scrolling 
            document.querySelector('body').style.overflow = "auto";
    
        });
    });


    // for the like Buttons
    const likeButtons = document.querySelectorAll('#like-button');
    likeButtons.forEach((likeButton) => {

        // add event to like buttons 
        likeButton.addEventListener('click', function() {

            // hide the current like button
            this.style.display = "none";

            // get like count
            let likeCount = this.parentElement.querySelector('span');

            // update like count by 1
            likeCount.textContent = parseInt(likeCount.textContent) + 1;

            // get the like collerd button
            const colorLikeButton = this.parentElement.querySelector('#like-button-color');

            // show color like button 
            colorLikeButton.style.display = "block";

            // send data to server 
            updateLikeCounter(this, likeCount.textContent, csrfToken)

        });
    });

    const unlikeButtons = document.querySelectorAll('#like-button-color');
    unlikeButtons.forEach((unlikeButton) => {

        // add event listener 
        unlikeButton.addEventListener('click', function() {

            // hide the color button
            this.style.display = "none";

            // get like count
            let likeCount = this.parentElement.querySelector('span');

            // substart the like couter by 1
            likeCount.textContent = parseInt(likeCount.textContent) - 1;

            // get the like collerd button
            const likeButton = this.parentElement.querySelector('#like-button');

            // show color like button 
            likeButton.style.display = "block";

            updateLikeCounter(this, likeCount.textContent, csrfToken)
        });
    });

});


function updateLikeCounter(likeButton, likeCounter, csrfToken) {

    // get like button container
    const postId = likeButton.parentElement.dataset.postid;


    // send date to server 
    fetch(`like/${postId}`, {
        method: 'PUT', 
        headers: {
            'X-CSRFToken': csrfToken.value
        }, 
        body: JSON.stringify ({
            'likeCount': likeCounter, 

        })
    });
}

// add event listenere to scrolling
window.addEventListener('scroll', () => {

    // get the new post form 
    document.querySelector('#new-post-form').style.top = `${window.scrollY}` +  'px';

});
