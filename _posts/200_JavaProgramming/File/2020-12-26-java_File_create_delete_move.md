---
title: Java - File - Create, Move, Rename, Delete
category: java 
tags: java programming File
---

## Java - File - Create, Mkdir, Rename, Delete

- Java에서 File 혹은 Directory를 만들고 이름을 바꾸고 지우는 방법을 설명합니다.

```java
import java.io.File;

class Main {
    public static void main(String[] args) throws Exception {

        // CREATE FILE
        // File Objectdml .createNewFile()을 사용해서 새로운 File을 만들어줍니다.
        String newFileName = "newFile.txt";
        File file = new File(newFileName);
        // .exists(): 파일이 존재하는지 확인하여 boolean을 리턴
        // 하지만, .exist()의 경우 자주 사용되지는 않습니다.
        System.out.println( file.exists() ); // false
        // .createNewFile(): file을 만들고, 만들어졌으면 true, 아니면 false를 리턴
        boolean isFileCreationSuccessful = file.createNewFile();
        if (isFileCreationSuccessful) {
            System.out.printf("Yeah, new File %s was made\n", newFileName);
        } else {
            System.out.printf("File %s already Exists\n", newFileName);
        }
        System.out.println("********************************************");


        // RENAME FILE
        // .renameTo()를 사용하면 되기는 하는데, String을 넘겨주는 것이 아니라,
        // 새로운 File을 열어서 넘겨줘야 합니다.
        String originalFileStr = "newFile.txt";
        File originalFile = new File(originalFileStr);

        String renamedFileStr = "newFileRenamed.txt";
        File renamedFile = new File(renamedFileStr);

        boolean isRenamed = originalFile.renameTo(renamedFile);
        if (isRenamed) {
            System.out.printf("Yeah, File %s was renamed to %s \n", originalFileStr, renamedFileStr);
        } else {
            System.out.printf("No, File %s can't be renamed to %s \n", originalFileStr, renamedFileStr);
        }
        System.out.println("********************************************");


        // REMOVE FILE
        // .delete 를 이용하서 file을 삭제할 수 있습니다.
        String fileNameToRemove = "newFileRenamed.txt";
        File fileToRemove = new File(fileNameToRemove);
        boolean isFileDeleted = fileToRemove.delete();
        if (isFileDeleted) {
            System.out.printf("Yeah, new File %s was deleted\n", newFileName);
        } else {
            System.out.printf("File %s can't be deleted\n", newFileName);
        }
        System.out.println("********************************************");


        // CREATE NEW DIRECTORY
        // file, directory 구분없이 모두 File로 지칭됩니다.
        String newDirectoryName = "newDirectory";
        File directory = new File(newDirectoryName);
        boolean isDirSuccessful = directory.mkdir();
        if (isDirSuccessful) {
            System.out.printf("Yeah, new Dir %s was made \n", newDirectoryName);
        } else {
            System.out.printf("Dir %s already Exists \n", newDirectoryName);
        }
        System.out.println("********************************************");
    }
}
```
