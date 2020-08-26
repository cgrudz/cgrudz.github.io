<style>
.section .reveal .state-background {
   background: #ffffff;
}
.section .reveal h1,
.section .reveal h2,
.section .reveal p {
   color: black;
   margin-top: 50px;
   text-align: center;
}
</style>


An introduction to programming in R -- Part 2
========================================================
date: 08/31/2020
autosize: true
incremental: true
width: 1920
height: 1080

<h2 style="text-align:left"> Instructions:</h2>
<p style='text-align:left'>Use the left and right arrow keys to navigate the presentation forward and backward respectively.  You can also use the arrows at the bottom right of the screen to navigate with a mouse.<br></p>

<blockquote>
FAIR USE ACT DISCLAIMER:</br>
This site is for educational purposes only.  This website may contain copyrighted material, the use of which has not been specifically authorized by the copyright holders. The material is made available on this website as a way to advance teaching, and copyright-protected materials are used to the extent necessary to make this class function in a distance learning environment.  The Fair Use Copyright Disclaimer is under section 107 of the Copyright Act of 1976, allowance is made for “fair use” for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research.
</blockquote>


========================================================

<h2>Outline</h2>

* The following topics will be covered in this lecture:

 * A review of Dataframes
 * Factors
 * File I/O
 * Basic plotting



========================================================
<h2>Data structures -- a quick review</h2>

* We will start by picking up with the "cats" dataframe we studied in the last activity.


```r
cats <- data.frame(coat = c("calico", "black", "tabby"), 
                    weight = c(2.1, 5.0, 3.2), 
                    likes_string = c(1, 0, 1))
```

* Notice that the arguments of the function "data.frame()" are three expressions associating a name with a vector.


========================================================
<h3>Dataframes</h3>

* Printing the variable "cats", we see what tabular data looks like in a dataframe:


```r
cats
```

```
    coat weight likes_string
1 calico    2.1            1
2  black    5.0            0
3  tabby    3.2            1
```

* The assignment of the vectors to names in the arguments assigned the column names.

* Each column consists of <b>a vector of uniform data type</b>.

* If we want to extract a named column from a dataframe, this can be done with the "$" sign and the column name:


```r
cats$weight
```

```
[1] 2.1 5.0 3.2
```

* Each row, on the other hand, consists of multiple measurements (of different data types) corresponding to one specific case of the data set.


========================================================
<h3>Dataframes -- continued</h3>

* We might suppose that the scale used to measure the cats' weights was off by two kgs.

* In this case, we can re-assign values into the column weight as follows:


```r
cats$weight
```

```
[1] 2.1 5.0 3.2
```

```r
cats$weight <- cats$weight + 2
```

* We can verify that the assignment went into the column for weight in "cats",


```r
cats
```

```
    coat weight likes_string
1 calico    4.1            1
2  black    7.0            0
3  tabby    5.2            1
```

========================================================
<h2>Lists </h2>

* A data structure related to vectors are <b>lists</b>.

* Lists function as containers for heterogeneous data, allowing different types:


```r
list_example <- list(1, "a", TRUE, 1+4i)
list_example
```

```
[[1]]
[1] 1

[[2]]
[1] "a"

[[3]]
[1] TRUE

[[4]]
[1] 1+4i
```

========================================================
<h3>Lists -- continued </h3>

* In the last example no type coercion has taken place; 


```r
typeof(list_example[[1]])
```

```
[1] "double"
```

```r
typeof(list_example[[2]])
```

```
[1] "character"
```

  * all of the original types have been respected, but because the data is allowed to be inhomogeneous we can't use vector operations on a list.
  

```r
list_example + 2
```

```
Error in list_example + 2: non-numeric argument to binary operator
```

* Here we see an error message because the "+" operator only knows how to operate on numeric arguments, or ones that can be coerced into one.

========================================================
<h3>Lists -- continued </h3>

* Recall our dataframe cats,


```r
cats
```

```
    coat weight likes_string
1 calico    4.1            1
2  black    7.0            0
3  tabby    5.2            1
```

* We know that dataframes contain homogeneous data in each <b>column</b>, but each row may be inhomogeneous.

* <b>Q:</b>What kind of data structure do you think a dataframe is? Can it be a vector? Why or why not?

* <b>A:</b> A dataframe cannot be a vector because of coercion rules --- instead it operates as a <b>list of vectors</b>:


```r
typeof(cats)
```

```
[1] "list"
```

```r
typeof(cats$weight)
```

```
[1] "double"
```

========================================================
<h2>Factors</h2>

* Consider now the vector "coat" in the dataframe:


```r
cats$coat
```

```
[1] calico black  tabby 
Levels: black calico tabby
```

```r
typeof(cats$coat)
```

```
[1] "integer"
```

```r
as.numeric(cats$coat)
```

```
[1] 2 1 3
```

* <b>Q:</b> can you hypothesize what the meaning is of this data? What is a level, and why are the coats "integer"?

* <b>A:</b> R likes to treat character strings in dataframes as categorical variables;

  * in this case, the categories are "black", "calico" and "tabby";
  
  * each integer value is encoding whether the case (or row) belongs to category 1, 2 or 3, where category labels are sorted alphanumerically.

========================================================
<h2>Manipulating dataframes</h2>

* Let's suppose that we need to include more information on our cats in our analysis; 
  
  * a friend has provided ages of all the cats for us:


```r
age <- c(2, 3, 5)
```

* We want to combine this into our dataframe, which can be done with "cbind()"


```r
cats <- cbind(cats, age)
cats
```

```
    coat weight likes_string age
1 calico    4.1            1   2
2  black    7.0            0   3
3  tabby    5.2            1   5
```

* This function introduces the new vector as an additional column in the dataframe; 

 * the variable name is defined the column name, and we reassign the dataframe to cats recursively.

========================================================
<h3>Adding columns to dataframes</h3>


* <b>Q:</b> can you hypothesize what will be the output if we try to combine the following vector with the dataframe?


```r
age <- c(2, 3, 5, 8, 9)
cats <- cbind(cats, age)
```

* <b>A:</b> dataframes, like matrices, need to have consistent dimensions of the data;

  * this new column is too long, so we will get an error:


```r
age <- c(2, 3, 5, 8, 9)
cats <- cbind(cats, age)
```

```
Error in data.frame(..., check.names = FALSE): arguments imply differing number of rows: 3, 5
```

========================================================
<h3>Dataframe dimensions</h3>

* We can examine the dimensions of a dataframe with standard functions:


```r
dim(cats)
```

```
[1] 3 4
```

* In the above we see the standard, matrix style dimensions of the dataframe.

  * these can also be extracted individually with "nrow" and "ncol":


```r
nrow(cats)
```

```
[1] 3
```

```r
ncol(cats)
```

```
[1] 4
```

========================================================
<h3>Dataframe indices</h3>

* Entries of dataframes can be accessed directly using matrix indexing:


```r
cats[2,4]
```

```
[1] 3
```

* This can also be performed with slices:

```r
cats[1:2, 2:3]
```

```
  weight likes_string
1    4.1            1
2    7.0            0
```

========================================================
<h3>Dataframe indices</h3>

* Additionally, we can use specialized notation for accessing an entire row or column:


```r
cats[,1]
```

```
[1] calico black  tabby 
Levels: black calico tabby
```

```r
cats[1,]
```

```
    coat weight likes_string age
1 calico    4.1            1   2
```

* Here, the blank in the place of the index tells R to extract the entire row or column.

========================================================
<h3>Adding rows to dataframes</h3>

* Let's suppose we have examined a new cat and we want to add a case to our dataframe:


```r
newRow <- list("tortoiseshell", 3.3, TRUE, 9)
cats <- rbind(cats, newRow)
cats
```

```
    coat weight likes_string age
1 calico    4.1            1   2
2  black    7.0            0   3
3  tabby    5.2            1   5
4   <NA>    3.3            1   9
```

* Notice, the "NA" value in the above for the coat of the fourth cat.

  * While the row was added successfully, it produces a "Not Available", missing data entry.
  
* Factors, like other vectors, are strict in R;

  * when we attempt to add a value that is not recognized as one of the categories, R treats this as missing data.


========================================================
<h3>Adding levels to factors</h3>

* We can access the levels of a factor vector with the "levels()" function:


```r
levels(cats$coat)
```

```
[1] "black"  "calico" "tabby" 
```

* If we want to re-assign new levels to a factor, we can do so recursively


```r
levels(cats$coat) <- c(levels(cats$coat), "tortoiseshell")
cats <- rbind(cats, list("tortoiseshell", 3.3, TRUE, 9))
cats
```

```
           coat weight likes_string age
1        calico    4.1            1   2
2         black    7.0            0   3
3         tabby    5.2            1   5
4          <NA>    3.3            1   9
5 tortoiseshell    3.3            1   9
```

* Notice, "tortiseshell" was now accepted as a category, but the NA value remains.

========================================================
<h3>Summarizing dataframes</h3>

* In general, we want to know if a dataframe has missing values, and what kind of variables are in it.

* Several common functions allow this, including

  * "str()" or the structure function:


```r
str(cats)
```

```
'data.frame':	5 obs. of  4 variables:
 $ coat        : Factor w/ 4 levels "black","calico",..: 2 1 3 NA 4
 $ weight      : num  4.1 7 5.2 3.3 3.3
 $ likes_string: num  1 0 1 1 1
 $ age         : num  2 3 5 9 9
```

* This tells us what the dimensions are, the column names are, and what types of variables we are working with.

========================================================
<h3>Summarizing dataframes -- continued</h3>

* We can also obtain a quick statistical summary of the data with the "summary()" function:


```r
summary(cats)
```

```
            coat       weight      likes_string      age     
 black        :1   Min.   :3.30   Min.   :0.0   Min.   :2.0  
 calico       :1   1st Qu.:3.30   1st Qu.:1.0   1st Qu.:3.0  
 tabby        :1   Median :4.10   Median :1.0   Median :5.0  
 tortoiseshell:1   Mean   :4.58   Mean   :0.8   Mean   :5.6  
 NA's         :1   3rd Qu.:5.20   3rd Qu.:1.0   3rd Qu.:9.0  
                   Max.   :7.00   Max.   :1.0   Max.   :9.0  
```

* The summary furthermore tells us how many missing values are present.

========================================================
<h3>Removing rows</h3>

* We will often want to remove cases with missing data;

  * this can be performed automatically with "na.omit()"
  

```r
na.omit(cats)
```

```
           coat weight likes_string age
1        calico    4.1            1   2
2         black    7.0            0   3
3         tabby    5.2            1   5
5 tortoiseshell    3.3            1   9
```

========================================================
<h3>Removing rows or columns</h3>

* We can also remove rows or columns by index, using a "-"


```r
cats[-1,]
```

```
           coat weight likes_string age
2         black    7.0            0   3
3         tabby    5.2            1   5
4          <NA>    3.3            1   9
5 tortoiseshell    3.3            1   9
```

```r
cats[,-1]
```

```
  weight likes_string age
1    4.1            1   2
2    7.0            0   3
3    5.2            1   5
4    3.3            1   9
5    3.3            1   9
```


========================================================
<h2>File IO</h2>

* Basic file input/ output (IO) can be done with functions such as:


```r
write.csv(x = cats, file = "feline-data.csv", row.names = FALSE)
cats_from_file <- read.csv(file = "feline-data.csv")
cats_from_file
```

```
           coat weight likes_string age
1        calico    4.1            1   2
2         black    7.0            0   3
3         tabby    5.2            1   5
4          <NA>    3.3            1   9
5 tortoiseshell    3.3            1   9
```

* In the above, we wrote the data cats to the file "feline-data.csv" in the data directory;

* CSV is a file type that R knows how to read automatically into a dataframe with the "read.csv()" function;
  
  * using the above command, we read the file into a new dataframe "cats_from_file".

========================================================
<h3>File IO -- continued</h3>

* We will suppose that we wish to analyze a new set of cat data that a friend gave us:

```
coat,   weight,     likes_string
calico, 2.1,        1
black,  5.0,        0
tabby,  3.2,        1
tabby,  2.3 or 2.4, 1
```

* Our friend was uncertain about the weight of the last cat and placed two values into the CSV.

* We suppose that this is written in the file "feline-data_v2.csv" which we will read with "read.csv()",


```r
cats_from_file <- read.csv(file="feline-data_v2.csv")
cats_from_file$weight
```

```
[1] 2.1        5.0        3.2        2.3 or 2.4
Levels: 2.1 2.3 or 2.4 3.2 5.0
```

* Notice that weight looks much different than before...

========================================================
<h3>Factors -- continued</h3>

* When R read the inhomogeneous data in the weights column, it first converted the values into character type;

  * when the character vector was seen by R in a dataframe, it then converted it automatically to a factor vector.
  
* Converting characters to factors automatically can be suppressed with additional arguments:


```r
cats_from_file <- read.csv(file="feline-data_v2.csv", stringsAsFactors=FALSE)
cats_from_file$weight
```

```
[1] "2.1"        "5.0"        "3.2"        "2.3 or 2.4"
```

* However, this illustrates in general how erroneously entered data can cause many issues with type conversions.

