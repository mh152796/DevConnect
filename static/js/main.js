  let searchForm = document.getElementById('searchForm')
  let pageLinks = document.getElementByClassName('page-link')

  if(searchForm){
    for(let i=0; pageLinks.length > i; i++)
    {
      pageLinks[i].addEventListener('click', function (e) {
        e.preventDefault()
        //GET THE DATA ATTRIBUTE
        let page = this.dataset.page

        //ADD HIDDEN SEARCH INPUT TO FROM
        searchForm.innerHTML +=`<input value=${page} name="page" hidden/>`
        //SUBMIT FROM
        searchForm.submit()
      })
    }
  }
