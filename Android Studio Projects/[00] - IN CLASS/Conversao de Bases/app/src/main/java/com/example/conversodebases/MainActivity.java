package com.example.conversodebases;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {
    TextView txtBase, txtNovaBase, txtNumeroConvertido;
    EditText txtNumeroOriginal;
    int aux1, aux2;

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


    // Inicialização de variáveis
    public void mainConfig() {
        txtNumeroOriginal = (EditText) findViewById(R.id.txtNumeroOriginal);
        txtNumeroConvertido = (TextView) findViewById(R.id.txtNumeroConvertido);
        txtBase = (TextView) findViewById(R.id.txtBase);
        txtNovaBase = (TextView) findViewById(R.id.txtNovaBase);
        aux1 = aux2 = 0;
    }


    public void alterarBase(View view) {
        txtBase.setText(CalculoDeBases.mudarBase(aux1));
        if (aux1 == 3)
            aux1 = 0;
        aux1++;
    }


    public void calcular(View view) {
        if (!txtNumeroOriginal.getText().toString().isEmpty()) {
            txtNumeroConvertido.setText(new CalculoDeBases().calcular(MainActivity.this));
            if (aux2 == 3)
                aux2 = 0;
            else
                aux2++;
        } else {
            txtNumeroConvertido.setText("Campo vazio ou \nvalor inválido!");
            txtNovaBase.setText("");
        }
    }
}