const fs = require('fs')

fs.readFile('./day7.txt', 'utf8' , (err, data) => {
    //console.log(bags);
    part1 = 0;
    bags = data.split("\r\n");
    //console.log(bags)
    var find = "shiny gold bag"
    var dict = {};
    bags.forEach(element => {
        bag_parts = element.split(" contain ")
        //console.log(bag_parts)
        main_bag = bag_parts[0]
        dict[main_bag] = []
        inside_bags = bag_parts[1].split(", ");
        inside_bags.forEach(element => {
            dict[main_bag].push(element);
        });
    });

    set = new Set();
    for (var key in dict) {
        for (var i = 0; i < dict[key].length; i++) {

            if(dict[key][i].includes(find) && set.){
                part1 +=1
                set.add(dict[key][i]);
            }
            else {
                //get the bags contained in this bag
            }
        }
    }
    console.log(part1);
})
//key will be bag name, values will be bag name