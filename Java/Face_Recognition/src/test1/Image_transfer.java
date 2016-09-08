package test1;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.net.URLEncoder;
import java.util.Base64;
import java.io.*;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class Image_transfer
 */
@WebServlet("/Image_transfer")
public class Image_transfer extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Image_transfer() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		System.out.println("Did a get request");
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		System.out.println("Did a post request");
		
		//code for decoding an image from byte format
		String pic = request.getParameter("base64URL");
		pic = URLEncoder.encode(pic, StandardCharsets.US_ASCII.toString());
		
		byte[] servdec = Base64.getEncoder().encode(pic.getBytes());
		OutputStream out = null;
		
		String path = "D:\\faces\\img.png";
		
		try {
		    out = new BufferedOutputStream(new FileOutputStream(path));
		    out.write(servdec);
		} finally {
		    if (out != null) out.close();
		}
		
		//call code for doing face recognition
		
		
		doGet(request, response);	//not necessarily needed if we implement a separate response for post and get
	}

}
