var a=new Vue({
             el:'#h_div' ,
          
              data: {
                      heading : "Corporate Seismic Data Repository System",
                      heading2:"Oil And Natural Gas Coorporation",
                      imgsrc : "images/ongc_logo.png"
                     },
            
      methods:{
     myFunction: function () {   
          window.open("homepage.html", "_self");    
      },
     myFunc: function () {   
          window.open("aboutus.html", "_self");    
      },
     myFunct: function () {   
          window.open("signup.html", "_self");    
      }
   }
         
               });

var b= new Vue({
        el:'#container',
        data: {
          Add: 'Add Entry',
          View: 'View Entry',
          Edit: 'Edit Entry',
          S: 'Survey',
          B: 'Block',
          A: 'Acquisition',
          M: 'Media',
        },
      });	
  var c=new Vue({
    el:'#survey',
    methods:{
      sur:function(){
        window.alert("Form Submitted");
      }
    }
  });



  