// Education adder

function addEdu() {
  const div = document.createElement('div');

  div.className = 'jumbotron';

  div.innerHTML = `
      <textarea name="school" type="text" placeholder="School/University" class="transFieldBig" ></textarea>
      <textarea name="degree" type="text" placeholder="Degree" class="transFieldSmall" rows=1></textarea>
      <textarea name="field" type="text" placeholder="Area of Study" class="transFieldMedium" rows=1></textarea>
      <textarea name="eduAbout" type="text" placeholder="Description" class="transFieldSmall"></textarea>
      <br>
      <input type="button" value="Remove" onclick="remover('education',this, 500)" class="btn btn-warning" />
      <br> <br>
      <input type="button" value="Add more" onclick="addEdu()" class="btn btn-success" />
  `;

  tingAdder('education', div, 500);
}

// Work adder 

function addWork() {
    const div = document.createElement('div');
  
    div.className = 'jumbotron';
  
    div.innerHTML = `
        <textarea name="company" type="text" placeholder="Company/Business/Organization" class="transFieldBig" ></textarea>
        <textarea name="job" type="text" placeholder="Job Title" class="transFieldMedium" rows=1></textarea>
        <textarea name="workAbout" type="text" placeholder="Description" class="transFieldSmall"></textarea>
        <br>
        <input type="button" value="Remove" onclick="remover('work',this, 500)" class="btn btn-warning" />
        <br> <br>
        <input type="button" value="Add more" onclick="addWork()" class="btn btn-success" />
    `;
  
    tingAdder('work', div, 500);

}
  

// Project adder 

function addProject() {
    const div = document.createElement('div');
  
    div.className = 'jumbotron';
  
    div.innerHTML = `
        <textarea name="projectTitle" type="text" placeholder="Project Title" class="transFieldMedium" rows=1></textarea>
        <textarea name="shortAbout" type="text" placeholder="Short Description" class="transFieldSmall" rows=1></textarea>
        <textarea name="longAbout" type="text" placeholder="Long Description (Optional)" class="transFieldSmall"></textarea>
        <br>
        <input type="button" value="Remove" onclick="remover('project', this, 500)" class="btn btn-warning" />
        <br> <br>
        <input type="button" value="Add more" onclick="addProject()" class="btn btn-success" />
    `;
    
    tingAdder('project', div, 500);
}
  


function tingAdder(elementId, input, speed){
    var category = document.getElementById(elementId);
    
    input.classList.add('greenHigh');

    if (category.childElementCount > 0) {
        category.insertBefore(input, category.firstElementChild);
}   else {
        category.appendChild(input);
    }

    setTimeout(function() {
        input.classList.remove('greenHigh');
    }, speed);

scroll(elementId)
}

function remover(category, input, speed) {
    toRemove = input.parentNode;

    var seconds = speed/1000;
    toRemove.style.transition = "opacity "+seconds+"s ease";
    toRemove.style.opacity = 0;
    toRemove.style.backgroundColor = "#AA0000";

    
    setTimeout(function() {
    document.getElementById(category).removeChild(toRemove);
}, speed);

}

function scroll(id){
    var scrollTo = document.getElementById(id);
    scrollTo.scrollIntoView({behavior: "smooth", block: "start"});
}

function scrollSubmit(){
    scroll(submitButton);
}

