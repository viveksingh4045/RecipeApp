function updatePreview(input) {
  let file = input.files[0];
  let reader = new FileReader();

  reader.readAsDataURL(file);
  reader.onload = function () {
      let img = document.getElementById('profilePrev');
      // can also use "this.result"
      img.src = reader.result;
  }
}

function recipePreview(input) {
 
  let file = input.files[0];
  let reader = new FileReader();

  reader.readAsDataURL(file);
  reader.onload = function () {
      let form_ins = document.getElementById('file_upload');
      form_ins.style.display = 'none';
      let imgPrev = document.getElementById('file_preview');
      imgPrev.style.display = 'block';
      alert('File found');
      let img = document.getElementById('recipeimgPreview');
      // can also use "this.result"
      img.src = reader.result;
  }
}


//let topPos = myElement.offsetTop;

function viewform(){
  let form = document.getElementsById('editprofile');
  form.style.display = 'block';
  form.scrollIntoView();
}
const editbtn = document.getElementsByClassName('editbtn')[0];
editbtn.addEventListener('click',openPopup);

function openPopup() {
  document.getElementById("popup").style.display = "flex";
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
}

