package com.example.allinclassapplications;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class CalculoIMCActivity extends AppCompatActivity {
    EditText txtPeso, txtAltura;
    TextView txtResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_calculoimc);

        txtPeso = (EditText) findViewById(R.id.txtPeso);
        txtAltura = (EditText) findViewById(R.id.txtAltura);
        txtResultado = (TextView) findViewById(R.id.txtResultado);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }

    public void calcularIMC(View view) {
        // Usando objeto
        //CalculoIMC cal = new CalculoIMC(txtPeso.getText().toString(), txtAltura.getText().toString());
        //txtResultado.setText("Seu IMC é de " + cal.resultado);

        // Usando método estático
        String resultado = CalculoIMC.calculaIMC(txtPeso.getText().toString(), txtAltura.getText().toString());
        txtResultado.setText(resultado);
    }
}