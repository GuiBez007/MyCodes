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

public class SituacaoActivity extends AppCompatActivity {
    EditText txtNome, txtFaltas, txtP1, txtP2, txtP3;
    TextView txtResultado;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_situacao);

        mainConfig();

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }


    private void mainConfig() {
        txtNome = (EditText) findViewById(R.id.txtNome);
        txtFaltas = (EditText) findViewById(R.id.txtFaltas);
        txtP1 = (EditText) findViewById(R.id.txtP1);
        txtP2 = (EditText) findViewById(R.id.txtP2);
        txtP3 = (EditText) findViewById(R.id.txtP3);
        txtResultado = (TextView) findViewById(R.id.txtResultado);
    }


    public void checarSituacao(View view) {
        txtResultado.setText(CalculoNotaFalta.calcular(this));
    }
}