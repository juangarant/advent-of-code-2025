import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Day01 {
    public static int combinacion (ArrayList<String> list) {
        int dial = 50;
        int contador = 0;
        for (String actual : list) {
            if (actual.charAt(0) == 'R') {
                dial = (dial + Integer.parseInt(actual.substring(1))) % 100;
            }
            else {
                dial = (dial - Integer.parseInt(actual.substring(1))) % 100;
            }
            if (dial == 0) {
                contador +=1;
            }
        }
        return contador;
    }

    public static void main (String[] args) {
        if (args.length != 1) {
            System.err.print("Debes usar: \"java day01.java <archivo>");
            return;
        }
        String path = args[0];
        try (BufferedReader bf = new BufferedReader(new FileReader(path))) {
            String linea;
            ArrayList<String> lista = new ArrayList<>();
            while ((linea = bf.readLine()) != null) {
                linea = linea.trim();
                lista.add(linea);
            }
            int sol = combinacion(lista);
            System.out.println(sol);
        } catch (IOException e) {
            System.err.print("Archivo no encontrado");
        }
    }
}