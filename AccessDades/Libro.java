package packet;

public class Libro {

	private String Titulo;
	private String Autor;
	private String AnyoNacimiento;
	private String AnyoPublicacion;
	private String Editorial;
	private String numPaginas;
	

	public Libro() {
		
	}


	public Libro(String titulo, String autor, String anyoNacimiento, String anyoPublicacion, String editorial,
			String numPaginas) {
		this.Titulo = titulo;
		this.Autor = autor;
		this.AnyoNacimiento = anyoNacimiento;
		this.AnyoPublicacion = anyoPublicacion;
		this.Editorial = editorial;
		this.numPaginas = numPaginas;
	}


	public String getTitulo() {
		return Titulo;
	}


	public void setTitulo(String titulo) {
		Titulo = titulo;
	}


	public String getAutor() {
		return Autor;
	}


	public void setAutor(String autor) {
		Autor = autor;
	}


	public String getAnyoNacimiento() {
		return AnyoNacimiento;
	}


	public void setAnyoNacimiento(String anyoNacimiento) {
		AnyoNacimiento = anyoNacimiento;
	}


	public String getAnyoPublicacion() {
		return AnyoPublicacion;
	}


	public void setAnyoPublicacion(String anyoPublicacion) {
		AnyoPublicacion = anyoPublicacion;
	}


	public String getEditorial() {
		return Editorial;
	}


	public void setEditorial(String editorial) {
		Editorial = editorial;
	}


	public String getNumPaginas() {
		return numPaginas;
	}


	public void setNumPaginas(String numPaginas) {
		this.numPaginas = numPaginas;
	}
	
}
	
