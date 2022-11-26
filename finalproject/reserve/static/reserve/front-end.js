async function getData(a, b, c, d) {
    try {const response = await fetch('/reserve', {
          method: 'POST',
          body: JSON.stringify({
            nationalCode: a,
            phoneNumber: b,
            dateNobat: c,
            doctorId: d,
          })
        })
    const data = await response.json();
    if (!response.ok) {
      console.log(response);
      throw new Error(`Error! status: ${response.message}`);
    }
    console.log(data);
  }
  catch(err) {
    console.log('***', err);
  }
  }
  document.addEventListener("DOMContentLoaded", function () {
    // document.querySelector('#date-input').style = 'none';
    document.querySelector('#btn-schedule').addEventListener("click", () => schedule())
    if (document.querySelector('#btn-reserve')) {

      document.querySelector('#btn-reserve').addEventListener("click", () => reserve())
    }

    if (document.querySelector('#btn-nobat')) {

      document.querySelector('#btn-nobat').addEventListener("click", () => myAppointment())
    }

    else {
      document.querySelector('#daily-schedule').style.display = 'none';

    }

    // document.addEventListener("click",event =>{
    //     const e = event.target;

    //     if(e.id == 'btn-reserve'){
    //         reserve()
    //     }

    //     if(e.id == 'btn-nobat'){
    //         myAppointment()
    //     }

    //     if(e.id == 'btn-schedule'){
    //         schedule()
    //     }



    // })
    if (document.querySelector('#btn-reserve')) {
      reserve()

    }
  })

  function reserve() {

    document.querySelector('#daily-schedule').style.display = 'none';
    document.querySelector('#my-nobat').style.display = 'none'
    document.querySelector('#reserve').style.display = 'block';

    // fetch('/reserve')
    // .then(res => res.json())
    // .then(result =>{
    // console.log(result)
    // //   console.error(error, '********')
    // document.querySelector('#reserve').innerHTML  += result.error
    // })

    document.querySelector('#reserve-form').onsubmit = function (e) {
      e.preventDefault();
      console.log(5678);
      // get values of post form && save in variables
      let naCode = document.querySelector("#na-code").value;
      let phNum = document.querySelector("#ph-num").value;
      let date = document.querySelector("#date-nobat").value;
      let drId = document.querySelector("#select-doctor").value;
      document.querySelector('#message-reserve').innerHTML = '';

      // console.log

      if(naCode=='' || phNum=='' || date=='' || drId==''){

          alert("Please fill all fields!")
      }

      else{

      if (new Date(date).valueOf() < new Date().valueOf()) {
        alert("The selected date has passed!")
      }

      else {
        console.log("1234");
        // fetch('/reserve',{
        //   method:'POST',
        //   bo
        // })



        fetch('/reserve', {
          method: 'POST',
          body: JSON.stringify({
            nationalCode: naCode,
            phoneNumber: phNum,
            dateNobat: date,
            doctorId: drId,
          })
        })
        .then(res => res.json())
        .then(result =>{

          console.log(result.error)
  
          if(result.error != ''){
            if(result.error != ''){
              document.querySelector('#message-reserve').innerHTML = '';
              document.querySelector('#message-reserve').innerHTML  += `<h6 style='color:red'>${result.error}</div>`
            }
            if(result.message != ''){
              document.querySelector('#message-reserve').innerHTML = '';
              document.querySelector('#message-reserve').innerHTML  += `<h6 style='color:green'>${result.message}</div>`

            }
              // alert(result.error)
          }
        })

        // getData(naCode,phNum,date,drId);

        // Clear out fields
        
      }

      }


    }
    document.querySelector("#na-code").value = '';
        document.querySelector("#ph-num").value = '';
        document.querySelector("#date-nobat").value = '';
        document.querySelector("#select-doctor").value = '';
  }

  function myAppointment() {
    document.querySelector('#reserve').style.display = 'none';
    document.querySelector('#daily-schedule').style.display = 'none';
    document.querySelector('#my-nobat').style.display = 'block';


    fetch('/mynobat')
      .then(res => res.json())
      .then(reserves => {
        console.log(reserves);
        if (reserves.error != undefined){

          document.querySelector('#my-nobat').innerHTML  = `<h6 style='color:red'>${reserves.error}</div>`

        }
        else{
          
          document.querySelector('#my-nobat').innerHTML = '';
          document.querySelector('#my-nobat').innerHTML += `<i><h3>My Appointments</h3></i>`;
  
          reserves.inf_turn.forEach(inf => {
  
            var div = document.createElement('div');
  
            div = ` <div class="col-12 border border-success" style=margin-bottom:5px; >
                      
                    <h6>Specialty:</h6> ${inf.specialty}
                    <h6>Doctor:</h6> ${inf.doctor_name}
                    <h6>Turn:</h6> ${inf.nobat}
                    <h6>Date:</h6> ${inf.date} 
                    <h6>Time:</h6> ${inf.time} 
  
              </div>`;
  
            document.querySelector('#my-nobat').innerHTML += div;
  
          })
        }
        
      })

  }

  function schedule() {

    if (document.querySelector('#reserve') && document.querySelector('#my-nobat')) {

      document.querySelector('#reserve').style.display = 'none';
      document.querySelector('#my-nobat').style.display = 'none';

    }
    document.querySelector('#daily-schedule').style.display = 'block';

    
    document.querySelector('#daily-form').onsubmit = function (e) {
      e.preventDefault();
      document.querySelector('#table-schedule').innerHTML = '';
      var div = document.createElement('div');
      let date0 = document.querySelector("#date-input").value;

      if (new Date(date0).valueOf() < new Date().valueOf()) {
        alert("The selected date has passed!")
      }

      else {

        fetch('/schedule', {
          method: 'POST',
          body: JSON.stringify({
            date: document.querySelector("#date-input").value
          })
        })

        fetch('/getschedule')
          .then(res => res.json())
          .then(doctors => {
            console.log(doctors)
            let flag = 0;
            if (doctors != '' && flag == 0) {

              doctors.forEach(doctor => {
                var div = document.createElement('div');

                div = `<div class="col-12 border border-danger" style= border:groove;margin-bottom:5px>
                        <h6>Specialty:</h6> ${doctor.specialty}
                        <h6>Doctor:</h6> ${doctor.doctor_name}
                        <h6>Capacity:</h6> ${doctor.capacity} 
                        <h6>Remained:</h6> ${doctor.mandeh}
                        <h6>Date:</h6> ${doctor.date} 
                        <h6>Time:</h6> ${doctor.time} 

                      </div> `

                document.querySelector('#table-schedule').innerHTML += div


              })
              
             
              flag = 1;
            
            }

            if(doctors == '' && flag == 0) {
              console.log('no')
              document.querySelector('#table-schedule').innerHTML = `<h5 style="color:red;">In this date there isn't doctor turn!</h5>`
              flag = 1;
            }
          })
      }

    }
  }