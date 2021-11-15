package packet;

import java.io.*;
import java.sql.*;
import java.util.ArrayList;

/**
 * 
 * @author Vicent Casasús Ejercicio Evaluable insertar datos de CSV a Base de
 *         Datos MySQL, XAMPP
 */
public class Main {

	/**
	 * En este metodo se consigue leer los datos del archivo csv.
	 * 
	 * @param ruta
	 * @return libros
	 * 
	 */
	public static ArrayList<Libro> leerCSV(String ruta) {

		ArrayList<Libro> libros = new ArrayList();
		// Lectura de datos del CSV
		try (BufferedReader br = new BufferedReader(new FileReader(ruta))) {
			String linea;
			int cont = 0;
			while ((linea = br.readLine()) != null) {
				if (cont >= 1) {
					// Las casillas del CSV es como si estuvieran separadas por ";".
					String[] atributos = linea.split(";");
					Libro libro = new Libro();

					libro.setTitulo(atributos[0]);
					libro.setAutor(atributos[1]);
					libro.setAnyoNacimiento(atributos[2]);
					libro.setAnyoPublicacion(atributos[3]);
					libro.setEditorial(atributos[4]);
					libro.setNumPaginas(atributos[5]);

					libros.add(libro);
				}
				cont++;
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

		return libros;
	}

	/**
	 * En el main ejecutamos la conexion a la Base de Datos e insertamos los libros
	 * dentro de ella. Luego hacemos dos consultas, una que saca los libros de los
	 * autores nacidos antes de 1950 y las editoriales que han publicado libros en
	 * el s. XXI.
	 * 
	 * @param args
	 */
	public static void main(String[] args) {

		ArrayList<Libro> libros = leerCSV("AE04_T1_4_JDBC_Dades.csv");
		int cont = 0;

		try {

			Class.forName("com.mysql.jdbc.Driver");
			Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost/biblioevaluable", "root", "");

			Statement s = conexion.createStatement();

			for (int i = 0; i < libros.size(); i++) {

				String titulo = libros.get(i).getTitulo();
				String autor = libros.get(i).getAutor();
				String anyoNacimiento = libros.get(i).getAnyoNacimiento();
				String anyoPublicacion = libros.get(i).getAnyoPublicacion();
				String editorial = libros.get(i).getEditorial();
				String numPaginas = libros.get(i).getNumPaginas();
				// Insercion de datos en BBDD
				PreparedStatement ps = conexion.prepareStatement(
						"INSERT INTO `libro` (`Titulo`, `Autor`, `AnyoNacimiento`, `AnyoPublicacion`, `Editorial`, `numPaginas`) VALUES (?,?,?,?,?,?)");
				ps.setString(1, titulo);
				ps.setString(2, autor);
				ps.setString(3, anyoNacimiento);
				ps.setString(4, anyoPublicacion);
				ps.setString(5, editorial);
				ps.setString(6, numPaginas);

				ps.executeUpdate();

				ps.close();
			}

			ResultSet rs = s.executeQuery(
					("SELECT `titulo`, `autor`, `anyoPublicacion` FROM `libro` WHERE `anyoNacimiento` < 1950"));
			System.out.println("Llibres (títol, autor i any de publicació) dels autors nascuts abans de 1950");
			while (rs.next()) {
				System.out.println(
						"TITULO: " + rs.getString(1) + " | AUTOR: " + rs.getString(2) + " | AÑO: " + rs.getString(3));
			}
			System.out.println(" ");
			rs = s.executeQuery(("SELECT `editorial` FROM `libro` WHERE `anyoPublicacion` >= 2001"));
			System.out.println("Editorials que hagen publicat almenys un llibre en el segle XXI.");
			while (rs.next()) {
				System.out.println("EDITORIALES: " + rs.getString(1));
			}

			rs.close();
			s.close();
			conexion.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println(" ");
		if (cont != 0) {
			System.out.println("Se han insertado los datos");
		} else {
			System.err.println("Error");
		}

	}

}