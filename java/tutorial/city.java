public class city { 
    public static Person[] arrAppend(Person[] arr, Person obj) {
        Person[] arrNew = new Person[arr.length + 1];
        int i;
        for(i = 0; i < arr.length; i++) {
            arrNew[i] = arr[i];
        }
        arrNew[i] = obj;
            
        return arrNew;
    }

    public static Building[] arrAppend(Building[] arr, Building obj) {
        Building[] arrNew = new Building[arr.length + 1];
        int i;
        for (i = 0; i < arr.length; i++) {
            arrNew[i] = arr[i];
        }
        arrNew[i] = obj;
            
        //print new array
        return arrNew;
    }

    static class Building {
        static int rooms;
        static int floors;
        static int block;
        static String name;
        static String shortname;

        public void init(int rooms_, int floors_, int block_, String name_, String shortname_) {
            rooms = rooms_;
            floors = floors_;
            block = block_;
            name = name_;
            shortname = shortname_;
        }
        // public void 
    };
    

    static class Person {
        static int age;
        static String name;
        static String job;
        static String office;
        static boolean employed;
        static boolean married;
        static String spouse;

        public void init(int age_, String name_, String job_, String office_, boolean employed_, boolean married_, String spouse_) {
            age = age_;
            name = name_;
            job = job_;
            office = office_;
            employed = employed_;
            married = married_;
            spouse = spouse_;
        }

        public void intro() {
            System.out.println("Hi! My name is " + name + ", and I am " + age + " years old.");
            if (employed) {
                if (job != null) {
                    System.out.println("I have a job as " + job + ".");
                }
                if (office != null) {
                    System.out.println("I work at " + office + ".");
                }
            }
            
            if (married) {
                System.out.println("I am married to " + spouse + ".");
            }
        }
    }

    static Building[] buildings = {};
    static Person[] people = {};

    public static void map() {
        System.out.println();
    };

    public static void main(String[] args) {

        Building School = new Building();
        School.init(15, 2, 2, "School", "School");


        Building WWTCenter = new Building();
        WWTCenter.init(5, 1, 1, "World Wide Technology Center", "WWT Center");

        Person AsherG = new Person();
        AsherG.init(12, "Asher Grossman", "the CEO of World Wide Technologies", "WWT Center", true, false, null);
        AsherG.intro();
        System.out.println();

        Person HenryG = new Person();
        HenryG.init(12, "Henry Grossman", "something probably", "someplace", true, false, null);
        HenryG.intro();
    }
}