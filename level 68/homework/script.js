   
    const contentDiv = document.getElementById("content");
    const firstChild = contentDiv.firstElementChild;
    if (firstChild) {
      contentDiv.removeChild(firstChild);
    }


    const ul = document.getElementById("myList");
    const lastLi = ul.lastElementChild;
    if (lastLi) {
      ul.removeChild(lastLi);
    }