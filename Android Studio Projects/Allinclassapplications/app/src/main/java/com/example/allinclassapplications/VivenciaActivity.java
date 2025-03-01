package com.example.allinclassapplications;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class VivenciaActivity extends AppCompatActivity {
    EditText txtNome;
    TextView txtResultado, txtNascimento;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_vivencia);

        mainConfig();

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }

    private void mainConfig() {
        txtNome = (EditText) findViewById(R.id.txtNome);
        txtNascimento = (TextView) findViewById(R.id.txtNascimento);
        txtResultado = (TextView) findViewById(R.id.txtResultado);
    }

    public void calcular(View view) {
        new CalculoVida().configurarDataNascimento(this, txtNascimento, (year, month, day) -> {
            Log.i("CHECK!", "CHECK3");
            txtNascimento.setText("Data de Nascimento: " + txtNascimento.getText().toString());
            txtResultado.setText(CalculoVida.calcularTempo());
        });
    }

}