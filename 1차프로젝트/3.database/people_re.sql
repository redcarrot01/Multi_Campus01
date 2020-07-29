// PYTHON_db 생성
use python_db

// people collection 생성
//db.createCollection("people")
db.createCollection("people1")

// isCapped() : 큰 사이즈로 설정됨
db.people1.isCapped()

// collection statis 정보 : 상태 정보를 볼 수 있음
db.people1.stats()

// emp collection 생성하고 drop
db.createCollection("emp")
// emp -> employees 로 rename
db.emp.renameCollection("employees")
db.emp.drop()

//document(row) 1개 추가 : (insertOne()) //새로고침해서 people 하단을 보면 필드가..
db.people1.insertOne({user_id:"bcd001", age:45, status:'A'})

//select * from people
db.people1.find()
db.people1.find({}) // 다보여줌 있는거 없는거 다

//select user_id,age from people { 조건} {}
db.people1.find({}, {user_id:1, age:1}) // 1이라는 건 컬럼을 보여라, _id는 항상 보여줌
//select user_id,status from people
db.people1.find({}, {user_id:1, status:1, _id:0}) //_id는 0으로 하면 안보여줌
// user_id와 status는 1은 줄 수 있지만 0으로 주진 않는다...
// document 여러개 insert : insertMany()
db.people1.insertMany([
    { user_id: "bcd002", age:25,status:"B" },
    { user_id: "bcd003", age:50,status:"A" },
    { user_id: "bcd004", age:35,status:"A" },
    { user_id: "abc001", age:28,status:"B" }  ])

db.people1.find().limit(2)
////////////////////////////////////////////// 연습///////////////////////////
//select * from people where status='A'
db.people1.find({status:'A'})
//select user_id, status from people where status='A'
db.people1.find({status:'A'},{user_id:1, status:1, _id:0})
// select * from people where status != 'A'
db.people1.find({status:{$ne:'A'} })
// select user_id, status, age from people user_id!='abc001'
db.people1.find({user_id:{$ne:'abc001'}},{user_id:1, status:1, age:1, _id:0})
// select * from people where status='A' and age=50
db.people1.find({status:'A', age:50})
// select * from people where status='A' or age=50
db.people1.find({$or:[{status:'A'},{age:50}]})
// select status, age from people where status='A' or age=50
db.people1.find({$or:[{status:'A'},{age:50}]},{status:1, age:1, _id:0})
//select * from people where age>25
db.people1.find({age:{$gt:25}})
//select * from people where age < 50
db.people1.find({age:{$lt:50}})
//select * from people where age >25 and age<50
db.people1.find({age:{$gt:25 ,$lt:50} })
//select * from people where age in (5, 15)
db.people1.find({age:{$in :[25,50]}})
//document 추가 status='C', user_id 민 포함한 document 추가(insetOne)
db.people1.insertOne({user_id: 'abc003',status:'C'})
db.people1.find()
//status 'A', 'C'
db.people1.find({status:{$in:['A','C']}})
//select * from people where age not in(5, 25)
db.people1.find({age:{$nin:[5, 25]}})
// select *from people where user_id like '%cd%'
db.people1.find({user_id:{$regex:/cd/}})
// select *from people where user_id like 'bc%'
db.people1.find({user_id:{$regex:/^bc/}}) //  /^로 시작하는
// select *from people where user_id like '%01'
db.people1.find({user_id:{$regex:/01$/}})   // o1로 끝나는
// select * from people status = 'A' order by USER_ID asc
db.people1.find({status:'A'}).sort({user_id:1})
// select user_id,age,status from people status = 'A' order by age desc
db.people1.find({status:'A'}, {user_id:1,age:1,status:1,_id:0}).sort({age:-1})
// select user_id,age from people where user_id like %cd% and age >40 order by user_id asc
db.people1.find({user_id:{$regex:/cd/}, age:{$gt:40}},{user_id:1, age:1, _id:0}).sort({user_id:1})
db.people1.find()
//select user_id,status,age from people where age>=25 and age<=45  and status in  ('A','B')
db.people1.find({age:{$gte:25},age:{$lte:45}, status:{$in:['A','B']}},{user_id:1, status:1, age:1,_id:0} )
//select count(*) from people
db.people1.count()
//select count(*) from people where age>30
db.people1.count({age:{$gt:30}})
//user_id 필드의 값이 존재하는 row count
db.people1.count({user_id:{$exists:true}})
db.people1.find({user_id:{$exists:true}})
//age 필드의 값이 존재하지 않는 row count
db.people1.count({age:{$exists:false}})
db.people1.find({age:{$exists:false}})
//select distinct(status) from people
db.people1.aggregate([{$group:{_id:"$status"}}]) //status 필드에 대해 그룹핑 한다 이때 _id는 status 같은 필드값 들어감

//findOne 이랑 find().limit() 동일
db.people1.findOne({age:{$gte:25}}) //한개만 출력
db.people1.find().limit(1)

db.people1.find().limit(3).skip(1) // 맨앞에 것만 스킵하고 나머지 순서대로 출력
db.people1.find()

//updateMany
//update people set status = 'C' where age>=45
db.people1.updateMany({age:{$gte:45}},{$set:{status:'C'}})
//update people set age=age+10 where status='B'
db.people1.updateMany({status:'B'},{$inc:{age:10}})
// updateOne
// update people set age = 100 where user_id = 'bcd001'
db.people1.updateOne({user_id:'bcd001'},{$set:{age:100}})
// update people set age = age+7 where status='B'
db.people1.updateOne({status:'B'}, {$inc:{age:7}})

// delete from people where status='C'
db.people1.deleteMany({status:'C'})

//
db.people1.updateMany({status:'B'}, {$set:{size:100}})

