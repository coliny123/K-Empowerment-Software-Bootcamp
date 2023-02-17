package ramda;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class ShapeTest {
    public static void main(String[] args) {
        List<Shape> rectagles = findShapes(Shape.shapes, s -> s.getType().equals("사각형"));
        System.out.print("사각형 :");
        System.out.println(rectagles);
        List<Shape> redNSmallShapes = findShapes(Shape.shapes, s -> s.getColor().equals("빨간색") && s.getArea() <= 12.0);
        System.out.print("빨간 도형(면적<=12.0): ");
        System.out.println(redNSmallShapes);
    }
    static List<Shape> findShapes(List<Shape> shapes, Predicate<Shape> p) {
        List<Shape> result = new ArrayList<>();

        for(Shape s : shapes){
            if(p.test(s)){
                result.add(s);
            }
        }
        return result;
    }
}
