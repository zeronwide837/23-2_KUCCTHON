function doAction() {
    let destinationURL = "./modal.html";
    window.location.href = destinationURL;
  }
  
  async function fetchData() {
    try {
      const myid = "user id 4";
      
    
  
      data1.forEach((item) => {
        console.log("User ID:", item.user_id);
        console.log("People:", item.people);
        console.log("percentage:", item.percentage);
        console.log("Soju Quantity:", item.soju_quantity);
        console.log("Beer Quantity:", data1.beer_quantity);
        console.log("Makguli Quantity:", data1.makguli_quantity);
        console.log("-----------"); // 항목 간 구분을 위해 추가
      });
  
      const sortedData = data1.sort((a, b) => b.percentage - a.percentage);
      let rankingContainer = document.querySelector("#ranking-container");
  
      console.log("Top 3 Users:");
      for (let i = 0; i < 3; i++) {
        let topUser = document.createElement("div");
        topUser.setAttribute("class", `rank rank-${i + 1}`);
  
        let topNum = document.createElement("div");
        topNum.setAttribute("class", "topNum");
        topNum.innerHTML = i + 1;
        topUser.appendChild(topNum);
  
        let myName = document.createElement("div");
        myName.setAttribute("class", "myName");
        myName.innerHTML = sortedData[i].user_id;
        topUser.appendChild(myName);
  
        let myPercent = document.createElement("div");
        myPercent.setAttribute("class", "myPercent");
        myPercent.innerHTML = sortedData[i].percentage;
        topUser.appendChild(myPercent);
  
        let mySoju = document.createElement("div");
        mySoju.setAttribute("class", "mySoju");
        mySoju.innerHTML = sortedData[i].soju_quantity;
        topUser.appendChild(mySoju);
  
        let topBeer = document.createElement("div");
        topBeer.setAttribute("class", "topBeer");
        topBeer.innerHTML = sortedData[i].beer_quantity;
        topUser.appendChild(topBeer);
  
        let myMakguli = document.createElement("div");
        myMakguli.setAttribute("class", "topMakjuli");
        myMakguli.innerHTML = sortedData[i].makguli_quantity;
        topUser.appendChild(myMakguli);
  
        console.log("User ID:", sortedData[i].user_id);
        console.log("Percentage:", sortedData[i].percentage);
        console.log("Soju Quantity:", sortedData[i].soju_quantity);
        console.log("Beer Quantity:", sortedData[i].beer_quantity);
        console.log("Makguli Quantity:", sortedData[i].makguli_quantity);
        console.log("-----------");
  
        rankingContainer.appendChild(topUser);
      }
  
      // myid에 해당하는 데이터 출력
      const myUserData = sortedData.find((user) => user.user_id === myid);
      const myRank = sortedData.indexOf(myUserData) + 1;
  
      let myUser = document.createElement("div");
      myUser.setAttribute("class", "myUser");
  
      let myNum = document.createElement("div");
      myNum.setAttribute("class", "myNum");
      myNum.innerHTML = myRank;
      myUser.appendChild(myNum);
  
      let myName = document.createElement("div");
      myName.setAttribute("class", "myName");
      myName.innerHTML = myUserData.user_id;
      myUser.appendChild(myName);
  
      let topPercent = document.createElement("div");
      topPercent.setAttribute("class", "topPercent");
      topPercent.innerHTML = myUserData.percentage;
      myUser.appendChild(topPercent);
  
      let mySoju = document.createElement("div");
      mySoju.setAttribute("class", "mySoju");
      mySoju.innerHTML = myUserData.soju_quantity;
      myUser.appendChild(mySoju);
  
      let myBeer = document.createElement("div");
      myBeer.setAttribute("class", "myBeer");
      myBeer.innerHTML = myUserData.beer_quantity;
      myUser.appendChild(myBeer);
  
      let myMakguli = document.createElement("div");
      myMakguli.setAttribute("class", "topMakjuli");
      myMakguli.innerHTML = myUserData.makguli_quantity;
      myUser.appendChild(myMakguli);
  
      rankingContainer.appendChild(myUser);
    } catch (error) {
      // console.error("Error:", error);
    }
  }
  
  // fetchData 함수 호출
  fetchData();