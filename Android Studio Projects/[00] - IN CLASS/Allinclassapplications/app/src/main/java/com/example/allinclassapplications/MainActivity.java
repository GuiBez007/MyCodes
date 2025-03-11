package com.example.allinclassapplications;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {
    Button button1, button2, button3, button4, button5, button6;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        mainConfig();

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }

    public void mainConfig() {
        button1 = (Button) findViewById(R.id.button1);
        button2 = (Button) findViewById(R.id.button2);
        button3 = (Button) findViewById(R.id.button3);
        button4 = (Button) findViewById(R.id.button4);
        button5 = (Button) findViewById(R.id.button5);
        button6 = (Button) findViewById(R.id.button6);
    }

    public void abrirTarefa1(View view) { // Primeiro app
        Intent VAR = new Intent(this, FirstActivity.class);
        startActivity(VAR);
    }

    public void abrirTarefa2(View view) { // Calculo IMC
        Intent VAR = new Intent(this, CalculoIMCActivity.class);
        startActivity(VAR);
    }
    public void abrirTarefa3(View view) { // Tempo Vivido
        Intent VAR = new Intent(this, VivenciaActivity.class);
        startActivity(VAR);
    }
    public void abrirTarefa4(View view) { // Situação do Aluno
        Intent VAR = new Intent(this, SituacaoActivity.class);
        startActivity(VAR);
    }
    public void abrirTarefa5(View view) { // Conversão de Bases
        Intent VAR = new Intent(this, ConversaoActivity.class);
        startActivity(VAR);
    }
    public void abrirTarefa6(View view) { // Login
        Intent VAR = new Intent(this, LoginActivity.class);
        startActivity(VAR);
    }
}