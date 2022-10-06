var httpRequest = require('request');
var xpath = require('xpath');
var xmldom = require('xmldom');
var xml2js = require('xml2js');

/* Set Test Data for api POST */
var apiTestData = [
    {'title':'foo','body':'bar','userId':1},
    {'title':'api input','body':'My second line','userId':2}
];

/* Loop through each item an call API POST function */
function listApiCallData(){
    for (let i=0; i<apiTestData.length; i++) {
        
		// Call the api function and return the results
		getApiData(apiTestData[i], function(b){
			console.log(b);
		});
        
    }
}

/* POST api data and return results via callback*/
var getApiData = function(strBody, callBack) {
    console.log(strBody);  // Testing that I received the correct string to POST

	/* FIXME: This is NOT waiting on the callBack but is moving to the next list item*/
	httpRequest.post(
		{
			url: "https://jsonplaceholder.typicode.com/posts",
			headers: {
				"Content-Type": "application/json;charset=UTF-8"
			},
            body: JSON.stringify(strBody),
			strictSSL: false

		}, function (error, response, body) {
				if (error) {
					// return error.toStrin();
					callBack(error.toString());
					// console.log(error.toString());

				}
				else if (response.statusCode == 201) {
                    // console.log(body);
					callBack(body);
					// return body;
				}
				else {
                    // console.log("There was another error");
					callBack("There was another error");
					// return "There was another error";
				}
			}
		); 

	
};


listApiCallData();
// getApiData();
