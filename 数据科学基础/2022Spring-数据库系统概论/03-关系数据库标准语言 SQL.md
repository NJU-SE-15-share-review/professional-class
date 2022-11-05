---
title: 03-关系数据库标准语言 SQL
categories:
    - 2022Spring-数据库系统概论
date: 2022-06-16 15:50:19
tags:
---

SQL 结构化查询语言，是关系数据库的标准语言。集数据定义语言（DDL），数据操纵语言（DML），数据控制语言（DCL）功能于一体。

仅有 9 个动词：`CREATE, DROP, ALTER, SELECT, INSERT, UPDATE, DELETE, GRANT, REVOKE`

## SQL 与关系数据库

![SQL 对关系数据库模式的支持](03-关系数据库标准语言 SQL/image-20220613201245493.png)

基本表是本身独立存在的表。一个关系对应一个基本表，一个或多个基本表对应一个存储文件，一个表可以带若干索引。

视图时从一个或几个基本表导出的表。数据库中只存放视图的定义而不存放视对应的数据。用户可以在视图上再定义视图。

## 层次化的数据库对象命名机制

1. 一个关系数据库管理系统的实例（Instance）中可以建立多个数据库（database）
2. 一个数据库中可以建立多个模式（schema）
3. 一个模式下通常包括多个表（table）、视图（view）和索引（index）等数据库对象

![层次化的数据库对象命名机制的层次结构](03-关系数据库标准语言 SQL/image-20220613201757227.png)

## 数据定义

![SQL的数据定义语句](03-关系数据库标准语言 SQL/image-20220613201858206.png)

### 定义模式

```SQL
CREATE SCHEMA <schemaName> AUTHORIZATION <username> [<table_defination_clause> | <view_defination_clause> | <authorization_defination_clause>]

# [例3.1] 为用户WANG定义一个学生-课程模式S-T
CREATE SCHEMA "S_T" AUTHORIZATION WANG;

# [例3.2] 该语句没有指定<模式名>，<模式名>隐含为<用户名>
CREATE SCHEMA AUTHORIZATION WANG; # 未指定模式名，默认为用户名

# [例3.3]为用户ZHANG创建了一个模式TEST，并且在其中定义一个表TAB1
CREATE SCHEMA TEST AUTHORIZATION ZHANG;
CREATE TABLE TAB1 (
    COL1 SMALLINT,
    COL2 INT,
    COL3 CHAR(20),
    COL4 NUMERIC(10,3),
    COL5 DECIMAL(5,2)
);
```

### 删除模式

```SQL
DROP SCHEMA <schemaName> <CASCADE | RESTRICT>

DROP SCHEMA WANG RESTRICT; # 只能删除空表，否则拒绝执行

# [例3.4] 删除模式ZHANG 同时该模式中定义的表TAB1也被删除
DROP SCHEMA ZHANG CASCADE;
```

## 定义基本表

```SQL
CREATE TABLE <tableName> (
    <colName> <datatype> [<col_integrity_constraints>]
    [,<colName> <datatype> [<col_integrity_constraints>]]
    ...
    [,<table_integrity_constraints>]
);

# [例3.5]  建立“学生”表Student。学号是主码，姓名取值唯一。
CREATE TABLE Student (
    Sno CHAR(9) PRIMARY KEY, # 列级完整性约束条件,Sno是主码, Sname取唯一值
    Sname CHAR(20) UNIQUE,
    Ssex CHAR(2),
    Sage SMALLINT,
    Sdept CHAR(20)
);

#  [例3.6] 建立一个“课程”表Course
CREATE TABLE Course (
    Cno CHAR(4) PRIMARY KEY,
    Cname CHAR(40) NOT NULL,
    Cpno CHAR(4),
    Ccredit SMALLINT,
    FOREIGN KEY (Cpno) REFERENCES Course(Cno)
);

# [例3.7]  建立一个学生选课表SC
CREATE TABLE SC (
    Sno CHAR(9),
    Cno CHAR(4),
    Grade SMALLINT,
    PRIMARY KEY (Sno,Cno), # 主码由两个属性构成，必须作为表级完整性进行定义
    FOREIGN KEY (Sno) REFERENCES Student(Sno), # 表级完整性约束条件，Sno是外码，被参照表是Student
    FOREIGN KEY (Cno)REFERENCES Course(Cno) # 表级完整性约束条件， Cno是外码，被参照表是Course
);
```

![](03-关系数据库标准语言 SQL/image-20220613203447480.png)

![](03-关系数据库标准语言 SQL/image-20220613203503801.png)

## 修改基本表

```SQL
ALTER TABLE <tableName>
	[ADD [COLUMN] <colName> <datatype> [<col_integrity_constraints>]] # 添加空值列
	[DROP [COLUMN] <colName> [CASCADE | RESTRICT]] # 删除列
	[ADD <table_integrity_constraints>] # 添加约束
	[DROP CONSTRAINT <integrity_constraints> [RESTRICT | CASCADE]] # 删除约束
	[ALTER COLUMN <colName> <datatype>]; # 修改列名或数据类型

# [例3.8] 向Student表增加“入学时间”列，其数据类型为日期型
ALTER TABLE Student ADD S_entrance DATE;

# [例3.9] 将年龄的数据类型由字符型（假设原来的数据类型是字符型）改为整数。
ALTER TABLE Student ALTER COLUMN Sage INT;

# [例3.10] 增加课程名称必须取唯一值的约束条件。
ALTER TABLE Course ADD UNIQUE(Cname);
```

## 删除基本表

```SQL
DROP TABLE <tableName> [RESTRICT | CASCADE];

#  [例3.11]  删除Student表
DROP TABLE Student RESTRICT; # 有其他对象依赖该表，不能删除

#  [例3.12] 若表上建有视图，选择RESTRICT时表不能删除;选择CASCADE时可以删除表，视图也自动删除。
DROP TABLE Student CASCADE; # 索引、视图、触发器等一并删除
```

## 索引

不在考试范围。

## 数据字典

数据字典是关系数据库管理系统内部的一组系统表，它记录了数据库中所有定义信息：关系模式定义 ，视图定义，索引定义，完整性约束定义，各类用户对数据库的操作权限，统计信息等。

## 数据查询

### 单表查询

`HAVING` 短语与 `WHERE` 子句的区别：作用对象不同。

`WHERE` 子句作用于基表或视图，从中选择满足条件的元组。

`HAVING` 短语作用于组，从中选择满足条件的组。

```SQL
SELECT [ALL | DISTINCT] <目标列表达式> [,<目标列表达式>] ...
	FROM <tableName> [,<tableName>] ... | (<select_caluse>)
	[AS] <alias>
	[WHERE <conditional_expression>]
	[GROUP BY <colName> [HAVING <conditional_expression>]]
	[ORDER BY <colName>] [ASC | DESC]];

# [例3.16]  查询全体学生的学号与姓名。
SELECT Sno, Sname FROM Student;

# [例3.17]  查询全体学生的姓名、学号、所在系。
SELECT Sname, Sno, Sdept FROM Student;

# [例3.18]  查询全体学生的详细记录
SELECT Sno, Sname, Ssex, Sage, Sdept FROM Student;
SELECT * FROM Student; # 与上一行等价

# [例3.19]  查全体学生的姓名及其出生年份。
SELECT Sname, 2014-Sage FROM Student;

# [例3.20] 查询全体学生的姓名、出生年份和所在的院系，要求用小写字母表示系名。
SELECT Sname, 'Year of Birth: ', 2014-Sage, LOWER(Sdept) FROM Student;
SELECT Sname NAME,'Year of Birth:' BIRTH, 2014-Sage BIRTHDAY, LOWER(Sdept) DEPARTMENT FROM Student; # 查询结果表头为别名

# [例3.21]  查询选修了课程的学生学号。
SELECT Sno FROM SC;
SELECT ALL Sno FROM SC; # 与上一行等价
SELECT DISTINCT Sno FROM SC;

# [例3.22] 查询计算机科学系全体学生的名单。
SELECT Sname FROM Student
WHERE Sdept=‘CS’;

# [例3.23]查询所有年龄在20岁以下的学生姓名及其年龄。
SELECT Sname, Sage FROM Student
WHERE Sage < 20;

# [例3.24]查询考试成绩有不及格的学生的学号。
SELECT DISTINCT Sn FROM SC
WHERE Grade < 60;

# [例3.25] 查询年龄在20~23岁（包括20岁和23岁）之间的学生的姓名、系别和年龄
SELECT Sname, Sdept, Sage FROM Student
WHERE Sage BETWEEN 20 AND 23;

# [例3.26]  查询年龄不在20~23岁之间的学生姓名、系别和年龄
SELECT Sname, Sdept, Sage FROM Student
WHERE Sage NOT BETWEEN 20 AND 23;

# [例3.27]查询计算机科学系（CS）、数学系（MA）和信息系（IS）学生的姓名和性别。
SELECT Sname, Ssex FROM Student
WHERE Sdept IN ('CS', 'MA', 'IS');

# [例3.28]查询既不是计算机科学系、数学系，也不是信息系的学生的姓名和性别。
SELECT Sname, Ssex FROM Student
WHERE Sdept NOT IN ('IS', 'MA', 'CS');

# [例3.29] 查询学号为201215121的学生的详细情况。
SELECT * FROM Student
WHERE Sno LIKE '201215121';
SELECT * FROM Student
WHERE Sno = '201215121'; # 与上一行等价

# [例3.30] 查询所有姓刘学生的姓名、学号和性别。
SELECT Sname, Sno, Ssex FROM Student
WHERE Sname LIKE '刘%'; # %匹配任意长度字符串

# [例3.31] 查询姓"欧阳"且全名为三个汉字的学生的姓名。
SELECT Sname FROM Student
WHERE Sname LIKE '欧阳_'; # _ 匹配任意单个字符

# [例3.32]  查询名字中第2个字为"阳"字的学生的姓名和学号。
SELECT Sname，Sno FROM Student
WHERE Sname LIKE '__阳%';

# [例3.33]  查询所有不姓刘的学生姓名、学号和性别。
SELECT Sname, Sno, Ssex FROM Student
WHERE Sname NOT LIKE '刘%';

#  [例3.34]  查询DB_Design课程的课程号和学分。
SELECT Cno，Ccredit FROM Course
WHERE Cname LIKE 'DB\_Design' ESCAPE '\ '; # ESCAPE '＼' 表示 '＼' 为换码字符

# [例3.35]  查询以"DB_"开头，且倒数第3个字符为 i的课程的详细情况。
SELECT * FROM Course
WHERE Cname LIKE 'DB\_%i_ _' ESCAPE '\ ';

# [例3.36]  某些学生选修课程后没有参加考试，所以有选课记录，但没有考试成绩。查询缺少成绩的学生的学号和相应的课程号。
SELECT Sno，Cno FROM SC
WHERE Grade IS NULL; # IS 不可换成 =

# [例3.38]  查询计算机系年龄在20岁以下的学生姓名。
SELECT Sname FROM Student
WHERE Sdept = 'CS' AND Sage < 20;

# [例3.27]  查询计算机科学系（CS）、数学系（MA）和信息系（IS）学生的姓名和性别。
SELECT Sname, Ssex FROM Student
WHERE Sdept IN ('CS', 'MA', 'IS');
SELECT Sname, Ssex FROM Student
WHERE Sdept = ' CS' OR Sdept = 'MA' OR Sdept= 'IS'; # 与上一行等价

# [例3.39] 查询选修了3号课程的学生的学号及其成绩，查询结果按分数降序排列。
SELECT Sno, Grade FROM SC WHERE Cno = '3'
ORDER BY Grade DESC;

# [例3.40]查询全体学生情况，查询结果按所在系的系号升序排列，同一系中的学生按年龄降序排列。
SELECT * FROM Student
ORDER BY Sdept, Sage DESC;

# [例3.41]  查询学生总人数。
SELECT COUNT(*) FROM Student;

# [例3.42]  查询选修了课程的学生人数。
SELECT COUNT(DISTINCT Sno)
FROM SC;

# [例3.43]  计算1号课程的学生平均成绩。
SELECT AVG(Grade) FROM SC
WHERE Cno = '1';

# [例3.44]  查询选修1号课程的学生最高分数。
SELECT MAX(Grade) FROM SC
WHERE Cno = '1';

# [例3.45] 查询学生201215012选修课程的总学分数。
SELECT SUM(Ccredit) FROM SC, Course
WHERE Sno = '201215012' AND SC.Cno = Course.Cno;

# [例3.46]  求各个课程号及相应的选课人数。
/* HAVING短语与WHERE子句的 区别：
	作用对象不同
	WHERE子句作用于基表或视图，从中选择满足条件的元组
	HAVING短语作用于组，从中选择满足条件的组。*/
SELECT Cno, COUNT(Sno) FROM SC
GROUP BY Cno;
SELECT Cno, COUNT(*) FROM SC
GROUP BY Cno;

# [例3.47]  查询选修了3门以上课程的学生学号。
SELECT Sno FROM SC
GROUP BY Sno
HAVING COUNT(*) > 3;

# [例3.48]查询平均成绩大于等于90分的学生学号和平均成绩
SELECT Sno, AVG(Grade) FROM SC GROUP BY Sno
HAVING AVG(Grade) >= 90;
```

![常用的查询条件](03-关系数据库标准语言 SQL/image-20220613210755589.png)

### 链接查询

```SQL
# [例 3.49] 查询每个学生及其选修课程的情况
SELECT Student.*, SC.* FROM Student, SC
WHERE Student.Sno = SC.Sno;

# [例 3.50] 对上例使用自然连接
SELECT Student.Sno,Sname,Ssex,Sage,Sd ept,Cno,Grade FROM Student,SC
WHERE Student.Sno = SC.Sno;

# [例 3.51]查询选修2号课程且成绩在90分以上的所有学生的学号和姓名。
SELECT Student.Sno, Sname
FROM Student, SC
WHERE Student.Sno = SC.Sno AND SC.Cno='2' AND SC.Grade > 90;

# [例 3.52]查询每一门课的间接先修课（即先修课的先修课）
SELECT FIRST.Cno, SECOND.Cpno
FROM Course FIRST, Course SECOND
WHERE FIRST.Cpno = SECOND.Cno;

# [例 3.53] 改写 [例 3.49]
# 左外连接：列出左表中所有的元组
SELECT Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade
FROM Student LEFT OUT JOIN SC ON (Student.Sno = SC.Sno);

# [例3.54]查询每个学生的学号、姓名、选修 的课程名及成绩
SELECT Student.Sno, Sname, Cname, Grade
FROM Student, SC, Course #多表连接
WHERE Student.Sno = SC.Sno
AND SC.Cno = Course.Cno;
```

### 嵌套查询

上层的查询块称为外层查询或父查询，下层查询块称为内层查询或子查询。

SQL 语言允许多层嵌套查询，即一个子查询中还可以嵌套其他子查询。如果子查询的查询条件不依赖于父查询，称为**不相关子查询**；否则称为**相关子查询**。

子查询的限制：**_不能使用 `ORDER BY` 子句_**。有些嵌套查询可以用连接运算替代，**谨慎使用嵌套查询**。

```SQL
# [例 3.55] 查询与“刘晨”在同一个系学习的学生。
# 不相关子查询
SELECT Sno, Sname, Sdept
FROM Student
WHERE Sdept IN (
    SELECT Sdept
    FROM Student
    WHERE Sname = '刘晨'
);

# 自身链接
SELECT S1.Sno, S1.Sname, S1.Sdept
FROM Student S1,
     Student S2
WHERE S1.Sdept = S2.Sdept
  AND S2.Sname = '刘晨';

# [例 3.56]查询选修了课程名为“信息系统”的学生学号和姓名
SELECT Sno, Sname
WHERE Sno IN (
    SELECT Sno
    FROM SC
    WHERE Cno IN (
        SELECT Cno
        FROM Course
        WHERE Cname = '信息系统'
    )
);

# 用连接查询实现[例 3.56]
SELECT Sno, Sname
FROM Student, SC, Course
WHERE Student.Sno = SC.Sno
  AND SC.Cno = Course.Cno
  AND Course.Cname = '信息系统';

# 在[例 3.55]中，由于一个学生只可能在一个系学习，则可以用 = 代替 IN：
SELECT Sno, Sname, Sdept
FROM Student
WHERE Sdept = (
    SELECT Sdept
    FROM Student
    WHERE Sname = '刘晨'
);

# [例 3.57] 找出每个学生超过他选修课程均成绩的课程号。
SELECT Sno, Cno
FROM SC x
WHERE Grade >= (
    SELECT AVG(Grade)
    FROM SC y
    WHERE y.Sno = x.Sno
);

# [例 3.58] 查询非计算机科学系中比计算机科学系任意一个学生年龄小的学生姓名和年龄
# 嵌套查询
SELECT Sname, Sage
FROM Student
WHERE Sdept <> 'CS'
AND Sage < ANY (
    SELECT Sage
    FROM Student
    WHERE Sdept = 'CS'
);

# 用聚集函数实现[例 3.58]
SELECT Sname, Sage
FROM Student
WHERE Sage < (SELECT MAX(Sage) FROM Student WHERE Sdept = 'CS ')
  AND Sdept <> 'CS';

# [例 3.59] 查询非计算机科学系中比计算机科学系所有学生年龄都小的学生姓名及年龄。
# 方法一：用ALL谓词
SELECT Sname, Sage
FROM Student
WHERE Sage < ALL (SELECT Sage FROM Student WHERE Sdept = 'CS')
  AND Sdept <> 'CS';

# 方法二：用聚集函数
SELECT Sname, Sage
FROM Student
WHERE Sage < (SELECT MIN(Sage) FROM Student WHERE Sdept = 'CS')
  AND Sdept <> 'CS';

# [例 3.60]查询所有选修了1号课程的学生姓名。
SELECT Sname
FROM Student
WHERE EXISTS(
              SELECT *
              FROM SC
              WHERE Sno = Student.Sno
                AND Cno = '1'
          );

#  [例 3.61] 查询没有选修1号课程的学生姓名。
SELECT Sname
FROM Student
WHERE NOT EXISTS(
        SELECT *
        FROM SC
        WHERE Sno = Student.Sno
          AND Cno = '1'
    );

# [例 3.55]查询与“刘晨”在同一 个系学习的学生。
SELECT Sno, Sname, Sdept
FROM Student S1
WHERE EXISTS(
              SELECT *
              FROM Student S2
              WHERE S2.Sdept = S1.Sdept
                AND S2.Sname = '刘晨'
          );

# [例 3.62] 查询选修了全部课程的学生姓名。
# 即，不存在没有修过的课程
SELECT Sname
FROM Student
WHERE NOT EXISTS(
        SELECT *
        FROM Course
        WHERE NOT EXISTS(
                SELECT * FROM SC WHERE Sno = Student.Sno AND Cno = Course.Cno
            )
    );

# [例 3.62] 改
SELECT Sname
FROM student
WHERE Sno IN (
    SELECT Sno
    FROM SC
    Group by Sno
    HAVING count(*) = (SELECT count(*) FROM course)
);
SELECT Sname
FROM Student
WHERE (SELECT COUNT(*) FROM course) = (
    SELECT COUNT(*) FROM SC
    GROUP BY Sno
    HAVING SC.Sno = Student.Sno
);

# [例 3.63]查询至少选修了学生 201215122选修的全部课程的学生号码。
# 不存在这样的课程y，学生201215122选修了y，而学生x没有选。
SELECT DISTINCT Sno
FROM SC SCX
WHERE NOT EXISTS(  # 学生201215122选修了而学生 x 没有选的课程
        SELECT *
        FROM SC SCY
        WHERE SCY.Sno = '201215122' AND NOT EXISTS(
                SELECT *  # 学生 x 选修的课程 y
                FROM SC SCZ
                WHERE SCZ.Sno = SCX.Sno
                  AND SCZ.Cno = SCY.Cno
            )
    );
```

### 集合查询

```SQL
# [例 3.64] 查询计算机科学系的学生及年龄不大于19岁的学生。
SELECT *
FROM Student
WHERE Sdept = 'CS'
UNION
SELECT *
FROM Student
WHERE Sage <= 19;

# [例 3.65] 查询选修了课程1或者选修了课程2的学生。
SELECT Sno
FROM SC
WHERE Cno = '1'
UNION
SELECT Sno
FROM SC
WHERE Cno = '2';

# [例3.66] 查询计算机科学系的学生与年龄不大于19岁的学生的交集。
SELECT *
FROM Student
WHERE Sdept = 'CS' INTERSECT
SELECT *
FROM Student
WHERE Sage <= 19;

# [例 3.66] 实际上就是查询计算机科学系中年龄不大于19岁的学生。
SELECT *
FROM Student
WHERE Sdept = 'CS'
  AND Sage <= 19;

# [例 3.67]查询既选修了课程1又选修了课程 2的学生。
SELECT Sno
FROM SC
WHERE Cno = '1' INTERSECT
SELECT Sno
FROM SC
WHERE Cno = '2';

# [例3.67]也可以表示为：
SELECT Sno
FROM SC
WHERE Cno = '1'
  AND Sno IN (
    SELECT Sno
    FROM SC
    WHERE Cno = '2'
);

# [例3.68]实际上是查询 计算机科学系中年龄大于19岁的学生
SELECT *
FROM Student
WHERE Sdept = 'CS'
  AND Sage > 19;
```

## 数据更新

### 数据插入

```SQL
INSERT INTO <表名> [(<属性列1>[, <属性列2 >...)]
VALUES (<常量1> [, <常量2>]... );

# [例3.69]将一个新学生元组（学号： 201215128;姓名：陈冬;性别：男; 所在系：IS;年龄：18岁）插入到 Student表中。
INSERT INTO Student (Sno, Sname, Ssex, Sdept, Sage)
VALUES ('201215128', '陈冬', '男', 'IS', 18);

# [例3.70]将学生张成民的信息插入 到Student表中。
INSERT INTO Student
VALUES ('201215126', '张成民', '男', 18, 'CS');

# [例3.71] 插入一条选课记录 （ '200215128','1 '）。
INSERT INTO SC(Sno, Cno)
VALUES ('201215128', '1');

# 或者
INSERT INTO SC
VALUES ('201215128', '1', NULL);

# [例3.72] 对每一个系，求学生的平均年龄，并把结果存入数据库
CREATE TABLE Dept_age
(
    Sdept CHAR(15) Avg_age SMALLINT
);
INSERT INTO Dept_age(Sdept, Avg_age)
SELECT Sdept.AVG(Sage)
FROM Student
GROUP BY Sdept;
```

### 数据修改

```SQL
UPDATE <表名>
SET <列名>=<表达式>[, <列名>=<表达式>].
..[WHERE <条件>];

# [例3.73] 将学生201215121的年龄改为22 岁
UPDATE Student
SET Sage = 22
WHERE Sno = ' 201215121 ';

# [例3.74] 将所有学生的年龄增加1岁。
UPDATE Student
SET Sage = Sage + 1;

# [例3.75] 将计算机科学系全体学生的成绩置零。
UPDATE SC
SET Grade = 0
WHERE Sno IN (SELETE Sno FROM Student WHERE Sdept = 'CS');
```

### 数据删除

```SQL
DELETE
FROM <表名> [WHERE <条件>];

# [例3.76] 删除学号为201215128的学生记录。
DELETE
FROM Student
WHERE Sno = '201215128';

# [例3.77] 删除所有的学生选课记录。
DELETE
FROM SC;

# [例3.78] 删除计算机科学系所有学生的选课记录。
DELETE
FROM SC
WHERE Sno IN (SELETE Sno FROM Student WHERE Sdept= 'CS');
```

## SQL 中的空值

判断空值用 `IS NULL` 或 `IS NOT NULL`。

有 `NOT NULL` 限制的 `UNIQUE` 属性不能为空值，码不能为空值。

空值与其他值的算术运算结果为空值，空值与其他值的比较运算结果为 `UNKNOWN`。

![逻辑运算符真值表](03-关系数据库标准语言 SQL/image-20220614183941402.png)

```SQL
# [例 3.83] 选出选修1号课程的不及格的学生以及缺考的学生。
SELECT Sno
FROM SC
WHERE Grade < 60
  AND Cno = '1'
UNION
SELECT Sno
FROM SC
WHERE Grade IS NULL
  AND Cno = '1';

# 或者
SELECT Sno
FROM SC
WHERE Cno = '1'
  AND (Grade < 60 OR Grade IS NULL);
```

## 视图

数据只存放视图的定义，不存放视图对应的数据。

视图的作用：

1. 视图能够简化用户的操作
2. 使用户能够以多种角度看待统一数据
3. 视图对重构数据库提供了一定程度的逻辑独立性
4. 试图能够对机密数据提供安全保护
5. 适当的利用视图可以更清晰地表达查询

### 定义视图

从单个基本表导出的、并且只是去掉了基本表的某些行和某些列，但保留了主码，这样的视图称为**行列子集视图**。

```SQL
CREATE VIEW <视图名> [(<列名> [,<列名>]...)]
AS <子查询> [WITH CHECK OPTION];
# WITH CKECK OPTION 表示对视图进行更新操作时要保证更新后的行满足谓词条件（即子查询中的条件）

# [例3.85]建立信息系学生 的视图，并要求进行修改 和插入操作时仍需保证该 视图只有信息系的学生。
CREATE VIEW IS_Student AS
SELECT Sno, Sname, Sage
FROM Student
WHERE Sdept = 'IS'
WITH CHECK OPTION;

# [例3.86] 建立信息系选修了1号课程的学生的视图（包括学号、 姓名、成绩）。
CREATE VIEW IS_S1(Sno, Sname, Grade) AS
SELECT Student.Sno, Sname, Grade
FROM Student,
     SC
WHERE Sdept = 'IS'
  AND Student.Sno = SC.Sno
  AND SC.Cno = '1';

# [例3.87] 建立信息系选修 了1号课程且成绩在90分 以上的学生的视图。
CREATE VIEW IS_S2 AS
SELECT Sno, Sname, Grade
FROM IS_S1
WHERE Grade >= 90;

# [例3.88] 定义一个反映学 生出生年份的视图。
CREATE VIEW BT_S(Sno, Sname, Sbirth) AS
SELECT Sno, Sname, 2014 - Sage
FROM Student;

# [例3.89] 将学生的学号及平 均成绩定义为一个视图
CREATE VIEW S_G(Sno, Gavg) AS
SELECT Sno, AVG(Grade)
FROM SC
GROUP BY Sno;

# [例3.90]将Student表中所有女生记 录定义为一个视图
# 修改基表Student的结构后，Student表与 F_Student视图 的映象关系被破坏，导致该视图不能正确工作。
CREATE VIEW F_Student(F_Sno, name, sex, age, dept) AS
SELECT * #不指定属性列
FROM Student
WHERE Ssex = '女';
```

### 删除视图

```SQL
DROP VIEW <视图名>[CASCADE];

# [例3.91 ] 删除视图BT_S和IS_S1
DROP VIEW BT_S; #成功执行
DROP VIEW IS_S1; #拒绝执行
DROP VIEW IS_S1 CASCADE;
# 成功执行
```

### 查询视图

**视图消解法**：进行有效性检查，从数据字典中取出视图的定义，把定义中的子查询和用户的查询结合起来，转换成等价的对基本表的查询，执行修正后的查询。

```SQL
# [例3.92] 在信息系学生的视 图中找出年龄小于20岁的学生。
SELECT Sno, Sage
FROM IS_Student
WHERE Sage < 20;
# 视图消解转换后的查询语句为：
SELECT Sno, Sage
FROM Student
WHERE Sdept = 'IS'
  AND Sage < 20;

# [例3.93] 查询选修了1号课 程的信息系学生
SELECT IS_Student.Sno, Sname
FROM IS_Student,
     SC
WHERE IS_Student.Sno = SC.Sno
  AND SC.Cno = '1';

# [例3.94]在S_G视图中查询平均成 绩在90分以上的学生学号和平均成绩
SELECT *
FROM S_G
WHERE Gavg >= 90;

# S_G视图的子查询定义：
SELECT Sno, AVG(Grade)
FROM SC
GROUP BY Sno;

# 错误：
SELECT Sno，AVG(Grade)
FROM SC
WHERE AVG(Grade) >= 90
GROUP BY Sno;

# 正确：
SELECT Sno, AVG(Grade)
FROM SC
GROUP BY Sno
HAVING AVG(Grade) >= 90;

# 或者使用派生表
SELECT *
FROM (SELECT Sno, AVG(Grade) FROM SC GROUP BY Sno) AS S_G(Sno, Gavg)
WHERE Gavg >= 90;
```

### 更新视图

允许对行列子集视图进行更新，对其他类型视图的更新不同系统有不同限制。

一般地，行列子集视图时可更新的。一些视图是不可更新的，因为对这些视图的更新不能唯一地有意义地转换成对相应基本表的更新。

一个不允许更新的视图上定义的视图也不允许更新。

```SQL
# [例3.95] 将信息系学生视图IS_Student中学号“201215122”的学生姓名改为“刘辰”。
UPDATE IS_Student
SET Sname= '刘辰'
WHERE Sno = '201215122';
# 转换后的语句：
UPDATE Student
SET Sname= '刘辰'
WHERE Sno = '201215122'
  AND Sdept = 'IS';

# [例3.96] 向信息系学生视图IS_S中插入一个新的学生 记录，其中学号为“201215129”，姓名为“赵新”，年龄 为20岁
INSERT INTO IS_Student
VALUES ('201215129', '赵新', 20);
# 转换为对基本表的更新：
INSERT INTO Student(Sno, Sname, Sage, Sdept)
VALUES ('200215129', '赵新', 20, 'IS');

# [例3.97]删除信息系学生视图IS_Student中学号 为“201215129”的记录
DELETE
FROM IS_Student
WHERE Sno = '201215129';
# 转换为对基本表的更新：
DELETE
FROM Student
WHERE Sno = '201215129'
  AND Sdept = 'IS';

# 例3.89定义的视图S_G为不可更新视图。
# 这个对视图的更新无法转换成对基本表SC的更新
UPDATE S_G
SET Gavg=90
WHERE Sno = '201215121';

# 将SC中成绩在平均成绩之上的元组定义成一个视图
CREATE VIEW GOOD_SC AS
SELECT Sno, Cno, Grade
FROM SC
WHERE Grade > (SELECT AVG(Grade) FROM SC);
```
