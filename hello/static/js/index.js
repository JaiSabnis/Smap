// Education adder


function addEdu() {
    const div = document.createElement('div');
  
     div.className = 'list-group-item';
  
    div.innerHTML = `
        <textarea name="school" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="School/Univeristy" class="transFieldBig" rows=1 required></textarea>
        <textarea name="degree" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Degree/Diploma" class="transFieldMedium" required></textarea>
        <textarea name="field" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Field(s) of Study" class="transFieldMedium" required></textarea>
        <textarea name="eduAbout" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Description (Optional)" class="transFieldMedium"  width= 100%></textarea>
        <div>
        <input type="button" value="Remove" onclick="remover('education',this.parentNode, 500)" class="btn btn-warning" />
        <input type="button" value="Add more" onclick="addEdu()" class="btn btn-success" />
        </div>

    `;
  
    tingAdder('education', div, 500);

}

function addWork() {
    const div = document.createElement('div');
  
     div.className = 'list-group-item';
  
    div.innerHTML = `
        <textarea name="company" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Company/Organization" class="transFieldBig" rows=1 required></textarea>
        <textarea name="job" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Job Title" class="transFieldMedium" required></textarea>
        <textarea name="workAbout" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Description" class="transFieldMedium"  ></textarea>
        <div>
        <h2>h</h2>
        <input type="button" value="Remove" onclick="remover('work',this.parentNode, 500)" class="btn btn-warning" />
        <input type="button" value="Add more" onclick="addWork()" class="btn btn-success" />
        </div>
    `;
  
    tingAdder('work', div, 500);

}



// Work adder 

function addWork() {
    const div = document.createElement('div');
  
     div.className = 'list-group-item';
  
    div.innerHTML = `
        <textarea name="company" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Company/Organization" class="transFieldBig" rows=1 required></textarea>
        <textarea name="job" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Job Title" class="transFieldMedium" required></textarea>
        <textarea name="workAbout" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Description" class="transFieldMedium"  ></textarea>
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
  
    div.className = 'card';
  
    div.innerHTML = `
        <img class="card-img-top" alt="Card image cap" src="https://study.com/cimages/multimages/16/02197d15-4c3b-4c7d-93cf-0958784ef512_group_project.jpeg"
        <div class="card-body">
        <textarea name="projectTitle" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"' type="text" placeholder="Project Title" class="transFieldBig" required rows=1></textarea>
        <textarea name="shortAbout" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"'type="text" placeholder="Short Description" class="transFieldMedium" required></textarea>
        <textarea name="longAbout" oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"'type="text" placeholder="Long Description (Optional)" class="transFieldMedium" required></textarea>
        <br>
        <input type="button" value="Remove" onclick="remover('project', this, 500)" class="btn btn-warning" />
        <br> 
        <input type="button" value="Add more" onclick="addProject()" class="btn btn-success" />
        </div>
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

function catParser(string){
    var bio =  document.getElementById('bio').value = "changed" ; 
    bio.value = string
}



/*
<div class="card bg-dark text-black"" style="border-radius: 1.5em;">
        <img class="card-img" alt="Card image cap" src="https://study.com/cimages/multimages/16/02197d15-4c3b-4c7d-93cf-0958784ef512_group_project.jpeg"
        <div class="card-img-overlay">
        <h5 name="postTitle" type="text" class="card-title">{{post.title}}</textarea>
        <p name="shortAbout" class="card-text" type="text">{{post.shortAbout}}</p>
        <p name="longAbout" class="card-text" type="text">{{post.longAbout}}</p>
        <br>
        <input type="button" value="Remove" onclick="remover('posts', this, 500)" class="btn btn-outline-warning" />
        <br> 
        <input type="button" value="Add new" onclick="location.href='{% url 'postCreate' %}';" class="btn btn-outline-success" />
        </div>
*/