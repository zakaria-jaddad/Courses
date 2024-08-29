document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');

  // * add event listener to the form submition of composition.
  document.querySelector('#compose-form').addEventListener('submit', function(event) {

    // preventing the page from reloading 
    event.preventDefault()

    // disable the button until everything is proccessed 
    const submitFormButton = document.querySelector('#compose-submit-button')
    submitFormButton.disabled = true

    fetch('/emails', {
      method: 'POST', 
      body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value, 
        subject: document.querySelector('#compose-subject').value, 
        body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(result => {
      
      // if ther is an error 
      if (result.error !== undefined) {
        showAlert(result.error);
      }
      // if the email is sent seccesfully 
      else {
        load_mailbox('sent');
        showAlert(result.message);
      }
    })
    
    // if there is any error 
    .catch(error => console.log(error));
    
    // * after the proccess is done unable the button, this is for preventing double submitons
    submitFormButton.disabled = false
  });
});



function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // changing the height of the conatiner
  document.querySelector('.bg-image-container').style.height = '28cm';

  // removing alerts 
  document.querySelector('#alert').style.display = 'none';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // remove alerts 
  document.querySelector('#alert').style.display = 'none';

  // cheking if sent to see the sent emails 
  if (mailbox === 'sent') {
    ShowMails("sent");
    document.querySelector('.bg-image-container').style.height = 'fit-content';
  }

  // render inbox

  if (mailbox === 'inbox') {
    ShowMails("inbox");
  }

  // render archive

  if (mailbox === 'archive') {
    ShowMails('archive')
  }
}


// ! this is for showing allerts 
function showAlert(value) {
  const alert = document.querySelector('#alert');

  document.querySelector('#alert').innerHTML = value;

  alert.style.display = 'block';
}


// ! this is for showing sent emails 
function ShowMails(category) {
  // could be {sent, mailbox, }

  // getting the emials container 
  const emailViews = document.querySelector('#emails-view')

  fetch(`emails/${category}`)
  .then(response => response.json())
  .then(emails => {
    emails.forEach((email) => {
      
      const emailBox = document.createElement('div');

      // spans inside div

      const span1 = document.createElement('span');
      span1.innerHTML = email.sender

      const span2 = document.createElement('span');
      span2.innerHTML = email.subject

      const span3 = document.createElement('span');
      span3.innerHTML = email.timestamp


      // add email id to a data-set
      emailBox.dataset.id = email.id;

      // add a class name to all of divs
      emailBox.className = 'sent-email';

      // checking if the emial has been read
      if (email.read === false)
        emailBox.style.backgroundColor = 'rgba(265, 265, 265, 0.4)';
      else {
        emailBox.style.backgroundColor = 'rgba(150, 150, 150, 0.4)';
        emailBox.style.color = 'white';
      }

      emailBox.appendChild(span1);
      emailBox.appendChild(span2);
      emailBox.appendChild(span3);

      // adding event to the div container wich i can have access to it  
      emailBox.addEventListener('click', function(){

        // email is clicked it means it is read so bakground color should change
        fetch(`emails/${this.dataset.id}`, {
          method: 'PUT', 
          body: JSON.stringify({
            read: true
          })
        })

        // if the user pressed the email container 
        // clear the email view and add email content to it

        fetch(`emails/${this.dataset.id}`)
        .then(response => response.json())
        .then(clickedEmail => {

          // * delete the container content and add the email content to it 
          // emailViews.innerHTML = clickedEmail.id;

          FromToSubjectTimestamp = [['From', clickedEmail.sender], 
                                      ['To', clickedEmail.recipients], 
                                      ['Subject', clickedEmail.subject], 
                                      ['Timestamp', clickedEmail.timestamp]];


          emailViews.innerHTML = '';
          // emial elments rendered using loop and shit 
          for (let i = 0; i < 4; i++) {

            const content = document.createElement('p');

            content.innerHTML = `<strong>${FromToSubjectTimestamp[i][0]} : </strong>` + FromToSubjectTimestamp[i][1];
            document.querySelector('#emails-view').appendChild(content);
          }

          // add a button, an hr, and then the body of the emial
          if (category !== 'sent') {

            // ! replay button
            const replayButton = document.createElement('button');
            replayButton.textContent = 'Replay';
            replayButton.className = "btn btn-sm btn-outline-primary nav-button";
            emailViews.appendChild(replayButton);

            // event listener to the replay button
            
            replayButton.addEventListener('click', () => {
              
              // email composition form 
              compose_email()

              // filling the inputs 
              document.querySelector('#compose-recipients').value = clickedEmail.sender;

              // subject 
              const composeSubject = document.querySelector('#compose-subject');
              if (!clickedEmail.subject.startsWith("Re: "))
                composeSubject.value = 'Re: ' + clickedEmail.subject;
              else  
                composeSubject.value = clickedEmail.subject;

                // body
                document.querySelector('#compose-body').value = 'On ' + clickedEmail.timestamp + ' ' + clickedEmail.sender + ' wrote: \n' + clickedEmail.body;
            });

            if (category !== 'archive') {
              // ! archived button
              const archivedButton = document.createElement('button');
              archivedButton.className = "btn btn-sm btn-outline-primary nav-button";
              archivedButton.textContent = 'Archive';         

              emailViews.appendChild(archivedButton);

              // event listener to the replay button
              
              archivedButton.addEventListener('click', () => {

                fetch(`emails/${clickedEmail.id}`, {
                  method: 'PUT',
                  body: JSON.stringify({
                    archived: true
                  })
                })
                .then(() => {
                  load_mailbox('inbox');
                  showAlert('Email is archived successfully');
                });


              });
            }
            else if (category === 'archive') {             
              // ! unarchived button
              const unarchivedButton = document.createElement('button');

              unarchivedButton.className = "btn btn-sm btn-outline-primary nav-button";
              unarchivedButton.textContent = 'Unarchive';         

              emailViews.appendChild(unarchivedButton);

              // ! event listener to unarchved button 
              unarchivedButton.addEventListener('click', () => {

                fetch(`emails/${clickedEmail.id}`, {
                  method: 'PUT', 
                  body: JSON.stringify({
                    archived: false
                  })
                })
                .then(() => {
                  load_mailbox('inbox');
                  showAlert('Email is unarchived successfully');
                });


              });
            }
          }  


          // ! hr 
          const hr = document.createElement('hr');
          hr.style.backgroundColor = '#fff';
          emailViews.appendChild(hr);

          // ! body
          const bodyParagraph = document.createElement('p');
          bodyParagraph.textContent = clickedEmail.body;
          emailViews.appendChild(bodyParagraph);

        });

      });

      emailViews.appendChild(emailBox)
    });
  });
}