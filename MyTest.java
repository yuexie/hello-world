import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;



public class MyTest{

    public static void printValue(String str){
        System.out.println("print value : " + str);
    }

    public static void main(String[] args) {
        
        List<String> listStr    = Arrays.asList("a","b","c","d");
        List<Integer> listInt   = Arrays.asList(11,23,45,33,45);

        String  str_result = getResult(listStr);
        Integer int_result = getResult(listInt);

        System.out.println(str_result);
        System.out.println(int_result);
        
        System.out.println("/*****************************/");

        Consumer<String> consumer = MyTest::printValue;
        listStr.forEach(consumer);

    }

    public static <T> T getResult(List<T> list){
        return list.get(0);
    }

}