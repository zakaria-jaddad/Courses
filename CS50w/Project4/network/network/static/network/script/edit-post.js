document.addEventListener('DOMContentLoaded', function() {

    let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0];

    // get the cancel button
    const cancelButtons = document.querySelectorAll('#cancel-edit-post');
    cancelButtons.forEach((Button) => {

        // add event listener to each cancel button 
        Button.addEventListener('click', function() {

            // hide the cancel button
            this.style.display = "none";

            // get the save button
            const saveButton = this.parentElement.firstElementChild;

            if (saveButton.textContent === "edit")
                return false  // do nothing.

            // change the textContent from save to edit 
            saveButton.textContent = "edit";

            Button.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('#edit-post-content').firstElementChild.value = Button.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('#post-content').textContent;

            // hide the edit-post-content 
            Button.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('#edit-post-content').style.display = "none";

            // show post conten 
            Button.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('#post-content').style.display = "block";
        });

    });

    // get edit button ==> function for edit posts
    const editPostButton = document.querySelectorAll('#edit-post');
    editPostButton.forEach((Button) => {

        // get the edit post form 
        const editPostForm = Button.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('#edit-post-content');

        // get post content Container
        const postContent = Button.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('#post-content');

        // click event for all edit buttons
        Button.addEventListener('click', function() {

            // get the cancel button
            const cancelButton = this.parentElement.lastElementChild;

            // edit button 
            if (this.textContent === 'edit') {

                // show the cance button
                cancelButton.style.display = "inline-block";

                // set form to display to block show form 
                editPostForm.style.display = "block";

                // hide post content 
                postContent.style.display = "none";

                // change button text Content to save
                Button.textContent = "save";
            }
            // if the button is save button 
            else if (this.textContent === 'save') {

                // hide cancel button
                cancelButton.style.display = "none";

                // get post new content
                const postNewContent = editPostForm.firstElementChild.value;

                if (postNewContent === '' || postNewContent.trim() === '') {
                    return false
                }

                // give new data to the server!!!!
                fetch("/", {
                    method: 'PUT', 
                    headers: {
                        'X-CSRFToken': csrfToken.value
                    },
                    body: JSON.stringify ({
                        postId: editPostForm.dataset.post, 
                        postContent: postNewContent
                    })
                })
                .then(response => {
                    return response.json();
                })
                .then(data => {
                    
                    // change post content to new content 
                    postContent.textContent = data.postContent;
                })

                // hide form 
                editPostForm.style.display = "none";

                // show post content
                postContent.style.display = "block";
                
                // change the content again to edit
                this.textContent = "edit";
            }

        });
    });
});