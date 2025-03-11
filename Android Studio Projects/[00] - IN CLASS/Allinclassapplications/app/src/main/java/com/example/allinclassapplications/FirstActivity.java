package com.example.allinclassapplications;

import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class FirstActivity extends AppCompatActivity {
    EditText txtDisciplina, txtNota1, txtNota2, txtFaltas;
    TextView txtMedia, txtSituacao;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_first);

        // My code
        txtDisciplina = (EditText) findViewById(R.id.txtDisciplina);
        txtNota1 = (EditText) findViewById(R.id.txtNota1);
        txtNota2 = (EditText) findViewById(R.id.txtNota2);
        txtFaltas = (EditText) findViewById(R.id.txtFaltas);
        txtMedia = (TextView) findViewById(R.id.txtMedia);
        txtSituacao = (TextView) findViewById(R.id.txtSituacao);
        //
        txtSituacao.setBackgroundColor(Color.BLACK);
        txtMedia.setBackgroundColor(Color.BLACK);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }

    public void calcularMedia(View view){
        try {
            float nota1 = Float.parseFloat(txtNota1.getText().toString());
            float nota2 = Float.parseFloat(txtNota2.getText().toString());
            txtMedia.setText(String.valueOf((nota1 + nota2) / 2));

            //                                                                   | pra não dar erro |txtFaltas.getText().toString().isEmpty() ||
            if (Float.parseFloat(txtMedia.getText().toString()) < 6 || Integer.parseInt(txtFaltas.getText().toString()) > 5) {
                txtSituacao.setText("REPROVADO!");
                txtMedia.setTextColor(Color.RED);
                txtSituacao.setTextColor(Color.RED);
            } else {
                txtSituacao.setText("APROVADO!");
                txtMedia.setTextColor(Color.GREEN);
                txtSituacao.setTextColor(Color.GREEN);
            }
        } catch(Exception e) {
            txtSituacao.setTextColor(Color.RED);
            txtSituacao.setText("Informação faltante!");
        }
    }


    public void apagarCampos(View view) {
        txtDisciplina.setText("");
        txtNota1.setText("");
        txtNota2.setText("");
        txtFaltas.setText("");
        txtMedia.setText("");
        txtSituacao.setText("");
    }
}