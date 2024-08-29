document.addEventListener('DOMContentLoaded', function() {

    // get all posts that exist in the view
    const allPostsContainers = document.querySelectorAll('.post-contianer');

    // execute this function each second
    // setInterval(function() {
    //     getLikeCounter(allPostsContainers);
    //     }, 1000
    // );


});

function getLikeCounter(allPostsContainers) {

    // loop over them and get their id
    allPostsContainers.forEach((container) => {
        
        // get post id 
        const postId = container.id;

        // get current like counter from the server 
        fetch(`${window.location.origin}/like/${postId}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }, 
            method: 'GET', 
        })
        .then(rsp => rsp.json())
        .then(data => {

            // get the likeCounter from html
            const likeCounter = container.querySelector('.likes-counter');
            likeCounter.textContent = data["likeCounter"];
        })
    });

}