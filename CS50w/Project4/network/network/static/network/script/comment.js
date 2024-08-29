window.addEventListener('load', function() {

    // get comment button
    const commentButtons = document.querySelectorAll('#comment');
    // itterate over all buttons
    commentButtons.forEach((commentButton) => {

        commentButton.addEventListener('click', function() {

            // get post container
            const postContainer = this.parentElement.parentElement.parentElement;

            // get comments sections
            const commentSection = postContainer.querySelector('#comment-section');

            // if the buttons color is white ==> ""
            if (this.style.fill === "") {

                // show comment section
                showCommentSection(commentSection);

                // change the comment button color 
                this.style.fill = "#199bef";
            }
            else {
                // hide comment sections
                hideCommentSection(commentSection);

                // change the comment button color 
                this.style.fill = "";
            }

        });
    });

    // hide comment section using canccel button
    document.addEventListener('click', function(event) {

        // check if event target is the cancel button
        if (event.target.id === 'cancel-comment') {
            event.preventDefault()
            // hide comment sections
            hideCommentSection(event.target.parentElement.parentElement.parentElement.parentElement)

            // cleare input
            event.target.parentElement.parentElement.querySelector('#comment-content').value = "";
            // get the show comment button
            const commentButton = event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('#comment');
            commentButton.style.fill = "";
        }
        return false
    });

    // unable the save comment button when user type something
    const commentFields = document.querySelectorAll('#comment-content');
    
    commentFields.forEach((commentField) => {

        // show buttons
        commentField.addEventListener('focus', function() {

            // show buttons
            showCommentButtons(this.parentElement.parentElement.lastElementChild)

        });

        // unable buttons
        commentField.addEventListener('keyup', function() {
            
            // get comment save button
            const commentSaveButton = this.parentElement.parentElement.querySelector('#save-comment');

            if (commentField.value != '' &&  commentField.value.trim(' ') != '') {
                commentSaveButton.disabled = false;
                commentSaveButton.style.backgroundColor = "#199bef";

            }
            else {
                commentSaveButton.disabled = true;
                commentSaveButton.style.backgroundColor = "#045082";
            }
            // get save comment buttons 

        });
    });


}); 


function hideCommentSection(commentSection) {
    // add
    commentSection.classList.add('hide-comment-section');

    // remove
    commentSection.classList.remove('show-comment-section');
}


function showCommentSection(commentSection) {
    // add
    commentSection.classList.add('show-comment-section');

    // remove
    commentSection.classList.remove('hide-comment-section');

}

function showCommentButtons(Buttons) {
    Buttons.classList.add('ds-f');
    Buttons.classList.remove('ds-n');

}