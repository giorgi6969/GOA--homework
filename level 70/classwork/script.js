    let num = 0;

    const myInterval = setInterval(function() {
      num += 2;
      console.log(num);


      if (num === 40) {
        clearInterval(myInterval);
      }
    }, 1500);