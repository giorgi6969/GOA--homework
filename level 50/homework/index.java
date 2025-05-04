  // Select all items
    const items = document.querySelectorAll('.item');
    
    // Add labels and click event
    items.forEach((item, index) => {
      item.textContent = index + 1;
      item.addEventListener('click', () => {
        // Generate random color
        const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
        item.style.background = randomColor;
      });
    });
