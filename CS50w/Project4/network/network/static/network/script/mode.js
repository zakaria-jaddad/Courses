document.addEventListener('DOMContentLoaded', function() {

    // get the value of a CSS variable
    const rootStyles = (document.documentElement);

    // check what Them
    if (localStorage.getItem('Them') === "light") {
        changeColorToLight(rootStyles);
        showIcon(`${localStorage.getItem('Them')}-mode`)
    }
    else if (localStorage.getItem('Them') === "dark") {
        changeColorToDark(rootStyles);
        showIcon(`${localStorage.getItem('Them')}-mode`)

    }

    // get the buttons
    const modeButtons = document.querySelectorAll('.mode');
    modeButtons.forEach((Button) => {

        // add event to the each button
        Button.addEventListener('click', function() {

            // check what button it is darck or light
            // if light mode it is 
            if (this.id === "light-mode") {
                changeColorToLight(rootStyles)
                // hide light button and show dark button
                hideButton(this);
                localStorage.setItem('Them', 'light');
            }
            // else dark mode it is
            else {
                changeColorToDark(rootStyles)
                // hide the dark buttons and show light button
                hideButton(this);
                localStorage.setItem('Them', 'dark');
            }
        });
    });
});

function showIcon(iconId) {
    document.querySelectorAll('.mode').forEach((button) => {

        // if the icons has the same id 
        if(button.id !== iconId) {
            button.classList.add('ds-b');
            button.classList.remove('ds-n');
        }
        else 
            hideButton(button);

    });
}

function changeColorToLight(rootStyles) {
    rootStyles.style.setProperty('--black-color', '#eee');
    rootStyles.style.setProperty('--white-color', '#000');
    rootStyles.style.setProperty('--second-white-color', '#505050');
    rootStyles.style.setProperty('--main-hover-dark-background-color', 'rgb(9, 9, 9, 10%)');
    rootStyles.style.setProperty('--border-color', '#C2CFD7');
}

function changeColorToDark(rootStyles) {
    rootStyles.style.setProperty('--black-color', '#000');
    rootStyles.style.setProperty('--white-color', '#fff');
    rootStyles.style.setProperty('--second-white-color', '#b9b9b9');
    rootStyles.style.setProperty('--main-hover-dark-background-color', 'rgb(231, 233, 234, 10%)');
    rootStyles.style.setProperty('--border-color', '#2f3337 ');
}

function hideButton(button) {
    // hide both buttons
    document.querySelectorAll('.mode').forEach(button => {

        button.classList.add('ds-b');
        button.classList.remove('ds-n');

    });

    // show the right button
    button.classList.add('ds-n');
    button.classList.remove('ds-b');
}
/* 

:root {
    --black-color : #000;
    --white-color : #fff;
    --second-white-color : #b9b9b9;
    --second-color : #199bef;
    --main-hover-dark-background-color : rgb(231, 233, 234, 10%) ;
}
darck mode
:root {
    --black-color : #eee;
    --white-color : #000;
    --second-white-color : #505050;
    --second-color : #199bef;
    --main-hover-dark-background-color : rgb(9, 9, 9, 10%) ;
}

*/
