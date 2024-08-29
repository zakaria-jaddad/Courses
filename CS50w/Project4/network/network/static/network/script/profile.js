document.addEventListener('DOMContentLoaded', function() {

    const profileBackButton = document.querySelector('#prfile-back-button');
    profileBackButton.addEventListener('click', function() {
        console.log('test')
        history.back()
    });

    try {

        // when the user clicks on the edit profile show them a form where to change the image or add it
        const ProfileButton = document.querySelector('#edit-profile-button');
        ProfileButton.addEventListener('click', function(event) {
            event.preventDefault();
    
            const editProfileForm = document.querySelector('#edit-profile-form');
    
            editProfileForm.classList.add('show-item');
    
            editProfileForm.classList.remove('remove-item');
    
            document.querySelector('body').style.overflow = "hidden";
        });
    }
    catch {
        // do nothing 
    }

});


// add event listenere to scrolling
window.addEventListener('scroll', () => {

    document.querySelector('#edit-profile-form').style.top = `${window.scrollY}` +  'px';

})