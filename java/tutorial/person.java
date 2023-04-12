public class Main {
    public static void main(String[] args) {
        class Person {
            String name1;
            String name2;
            int age;
            char favLetter;
            boolean normal;
            public void showAndTell() {
                System.out.println("Name: " + name1 + " " + name2);
                System.out.println("Age: " + age);
                System.out.println("Favorite Letter: " + favLetter);
                System.out.println("Normal?: " + normal);
            }
        };
        Person Asher = new Person();
        Asher.name1 = "Asher";
        Asher.name2 = "Grossman";
        Asher.age = 12;
        Asher.favLetter = 'A';
        Asher.normal = false;
        
        Asher.showAndTell();
    }
}