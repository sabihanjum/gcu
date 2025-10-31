let student = 
{
    name: "John Doe",
    age: 20,
    phoneNo: 1234567890,
}
console.log(student);
console.log(student.name); //accessing property
console.log(student["age"]); //accessing property

student.age = 21;
console.log(student.age); //modifying property

student.email = "john.doe@example.com";
console.log(student); //adding new property